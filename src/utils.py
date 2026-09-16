import logging
import time
from functools import wraps

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("smart_ai_chatbot")


# Input validation
def is_valid_input(user_text: str) -> bool:
    """True if the user's message has real content (not empty/whitespace-only)."""
    return bool(user_text and user_text.strip())


def clean_input(user_text: str) -> str:
    """Strips leading/trailing whitespace; returns '' for None."""
    return user_text.strip() if user_text else ""


# Response validation
_API_FALLBACK_MARKER = "Sorry, something went wrong"


def is_valid_response(response_text: str) -> bool:
    """True if the AI response text is non-empty and not the API's own fallback message."""
    if not response_text or not response_text.strip():
        return False
    return _API_FALLBACK_MARKER not in response_text


# Retry wrapper for failures (rate limits, brief network drops)
def with_retry(max_attempts: int = 2, delay_seconds: float = 1.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for attempt in range(1, max_attempts + 1):
                result = func(*args, **kwargs)
                if is_valid_response(result):
                    return result
                logger.warning(
                    "API call failed (attempt %d/%d) — retrying...",
                    attempt,
                    max_attempts,
                )
                if attempt < max_attempts:
                    time.sleep(delay_seconds)
            return result

        return wrapper

    return decorator


# Startup / config checks
def check_env_var(name: str, value: str) -> None:
    """
    Logs a clear, actionable message if a required environment variable
    is missing. Does not raise — callers decide how to react.
    """
    if not value:
        logger.error(
            "Missing required environment variable: %s. "
            "Add it to your .env file (see .env.example).",
            name,
        )
