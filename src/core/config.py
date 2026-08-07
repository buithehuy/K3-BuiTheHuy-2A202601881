"""
Lab 11 — Configuration & API Key Setup
"""
import os


def setup_api_key():
    """Load API key from environment or prompt."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    use_groq = os.environ.get("USE_GROQ", "0") == "1"
    
    if use_groq:
        if "GROQ_API_KEY" not in os.environ:
            os.environ["GROQ_API_KEY"] = input("Enter Groq API Key: ")
        print("Groq API key loaded.")
    else:
        if "GOOGLE_API_KEY" not in os.environ:
            os.environ["GOOGLE_API_KEY"] = input("Enter Google API Key: ")
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "0"
        print("Google API key loaded.")

def get_model_name() -> str:
    """Return the configured model name."""
    if os.environ.get("USE_GROQ", "0") == "1":
        # Note: adjust this to whichever Groq model you want to use
        return "groq/qwen/qwen3.6-27b"
    return "gemini-1.5-flash-8b"


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
