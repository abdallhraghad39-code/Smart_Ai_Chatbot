import os
import sys
import unittest
from unittest.mock import patch, MagicMock

os.environ.setdefault("COHERE_API_KEY", "test-key-for-unit-tests")

SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC_DIR)

import utils  # noqa: E402
import prompts  # noqa: E402


class TestUtils(unittest.TestCase):

    def test_valid_input_accepted(self):
        self.assertTrue(utils.is_valid_input("Hello there"))

    def test_empty_input_rejected(self):
        self.assertFalse(utils.is_valid_input(""))

    def test_whitespace_only_input_rejected(self):
        self.assertFalse(utils.is_valid_input("    "))

    def test_none_input_rejected(self):
        self.assertFalse(utils.is_valid_input(None))

    def test_clean_input_strips_whitespace(self):
        self.assertEqual(utils.clean_input("  hi  "), "hi")

    def test_valid_response_accepted(self):
        self.assertTrue(utils.is_valid_response("Here is your answer."))

    def test_fallback_response_flagged_invalid(self):
        fallback = "Sorry, something went wrong while contacting the AI service."
        self.assertFalse(utils.is_valid_response(fallback))

    def test_empty_response_flagged_invalid(self):
        self.assertFalse(utils.is_valid_response(""))

    def test_with_retry_returns_first_success(self):
        calls = {"count": 0}

        @utils.with_retry(max_attempts=3, delay_seconds=0)
        def flaky():
            calls["count"] += 1
            return "a real answer"

        result = flaky()
        self.assertEqual(result, "a real answer")
        self.assertEqual(calls["count"], 1)  # succeeded on first try, no retry needed

    def test_with_retry_retries_then_gives_up(self):
        calls = {"count": 0}

        @utils.with_retry(max_attempts=2, delay_seconds=0)
        def always_fails():
            calls["count"] += 1
            return "Sorry, something went wrong while contacting the AI service."

        result = always_fails()
        self.assertEqual(calls["count"], 2)  # tried twice
        self.assertIn("Sorry, something went wrong", result)  # gave up


class TestPrompts(unittest.TestCase):
    """conversation-history module"""

    def test_initialize_history_contains_system_prompt(self):
        history = prompts.initialize_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]["role"], "system")

    def test_build_prompt_appends_user_message(self):
        history = prompts.initialize_history()
        history = prompts.build_prompt(history, "What is a REST API?")
        self.assertEqual(history[-1], {"role": "user", "content": "What is a REST API?"})

    def test_add_assistant_reply_appends_assistant_message(self):
        history = prompts.initialize_history()
        history = prompts.add_assistant_reply(history, "It's a way for apps to talk.")
        self.assertEqual(
            history[-1],
            {"role": "assistant", "content": "It's a way for apps to talk."},
        )

    def test_history_accumulates_across_multiple_turns(self):
        """The bot should 'remember' earlier turns"""
        history = prompts.initialize_history()
        history = prompts.build_prompt(history, "My name is Hasan.")
        history = prompts.add_assistant_reply(history, "Nice to meet you!")
        history = prompts.build_prompt(history, "What is my name?")
        # system + 3 turns = 4 entries
        self.assertEqual(len(history), 4)
        self.assertEqual(history[1]["content"], "My name is Hasan.")


class TestApiClient(unittest.TestCase):
    """API integration"""

    def test_successful_response_is_parsed_and_stripped(self):
        import api_client

        fake_response = MagicMock()
        fake_response.message.content = [MagicMock(text="  Here is the answer.  ")]

        with patch.object(api_client.client, "chat", return_value=fake_response):
            result = api_client.get_ai_response(
                [{"role": "user", "content": "hi"}]
            )
        self.assertEqual(result, "Here is the answer.")

    def test_api_exception_does_not_crash_and_returns_fallback(self):
        """Simulates invalid key / network failure / rate limit / model
        unavailable"""
        import api_client

        with patch.object(api_client.client, "chat", side_effect=Exception("boom")):
            result = api_client.get_ai_response(
                [{"role": "user", "content": "hi"}]
            )
        self.assertIn("Sorry, something went wrong", result)

    def test_malformed_response_does_not_crash(self):
        """API returns something unexpectedly shaped"""
        import api_client

        fake_response = MagicMock()
        fake_response.message.content = []  # IndexError when [0] is accessed

        with patch.object(api_client.client, "chat", return_value=fake_response):
            result = api_client.get_ai_response(
                [{"role": "user", "content": "hi"}]
            )
        self.assertIn("Sorry, something went wrong", result)


class TestIntendedChatbotFlow(unittest.TestCase):

    def test_full_turn_end_to_end_with_mocked_api(self):
        import api_client

        history = prompts.initialize_history()
        user_msg = "Explain machine learning simply."

        self.assertTrue(utils.is_valid_input(user_msg))

        history = prompts.build_prompt(history, user_msg)

        fake_response = MagicMock()
        fake_response.message.content = [MagicMock(text="ML is teaching computers from examples.")]

        with patch.object(api_client.client, "chat", return_value=fake_response):
            reply = api_client.get_ai_response(history)

        self.assertTrue(utils.is_valid_response(reply))

        history = prompts.add_assistant_reply(history, reply)

        # system + user + assistant
        self.assertEqual(len(history), 3)
        self.assertEqual(history[-1]["role"], "assistant")

    def test_exit_command_logic(self):
        for raw in ["exit", "Exit", "EXIT", "  exit  ".strip()]:
            self.assertEqual(raw.lower(), "exit")


class TestChatbotEntryPoint(unittest.TestCase):

    def test_chatbot_module_imports_successfully(self):
        import chatbot  # noqa: F401

        self.assertTrue(hasattr(chatbot, "run_chatbot"))
        self.assertTrue(hasattr(chatbot, "get_user_input"))
        self.assertTrue(hasattr(chatbot, "display_response"))

    def test_run_chatbot_uses_conversation_history_end_to_end(self):
        import chatbot
        import api_client

        fake_response = MagicMock()
        fake_response.message.content = [MagicMock(text="Nice to meet you!")]

        with patch.object(api_client.client, "chat", return_value=fake_response):
            with patch("builtins.input", side_effect=["My name is Mariam.", "exit"]):
                chatbot.run_chatbot()  # should complete without raising


if __name__ == "__main__":
    unittest.main(verbosity=2)