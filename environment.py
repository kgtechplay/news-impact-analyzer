"""
Environment Configuration for News Impact Analyzer
Store all environment variables here for easy management
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.3"))

# Application Configuration
APP_NAME = os.getenv("APP_NAME", "News Impact Analyzer")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# Web Scraping Configuration
USER_AGENT = os.getenv("USER_AGENT", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", "4000"))

# Streamlit Configuration
PAGE_TITLE = os.getenv("PAGE_TITLE", "News Impact Analyzer")
PAGE_ICON = os.getenv("PAGE_ICON", "📊")
LAYOUT = os.getenv("LAYOUT", "wide")
STREAMLIT_SERVER_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", "8501"))
STREAMLIT_SERVER_ADDRESS = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")

# Analysis Configuration
IMPACT_SCORE_RANGE = (0, 10)  # Min and max impact scores
LISTED_OPTIONS = ["Y", "N"]  # Listed status options
IMPACT_TYPES = ["positive", "negative"]  # Valid impact types

# Default prompt template
DEFAULT_PROMPT_TEMPLATE = """
Analyze the following news content and identify Indian companies that could be impacted by this news.

Content: {content}

For each identified company, provide the following information in JSON format:
- company name: The exact name of the company
- impact type: "positive" or "negative" based on how the news affects the company
- company industry: The industry sector the company operates in
- impact score: A score from 0-10 where 10 is the highest impact
- listed: "Y" if the company is listed on BSE/NSE, "N" if not

Focus only on Indian companies and provide realistic impact assessments.
Return the results as a JSON array with the exact format specified above.

Example format:
[
    {{
        "company name": "Tata Motors",
        "impact type": "positive",
        "company industry": "Automotive",
        "impact score": 7,
        "listed": "Y"
    }}
]

If no relevant Indian companies are found, return an empty array [].
"""

def validate_config():
    """Validate that all required configuration is set"""
    if OPENAI_API_KEY == "your_openai_api_key_here":
        print("⚠️  Warning: OpenAI API key not configured!")
        print("   Please set OPENAI_API_KEY in your .env file")
        return False
    return True

def get_config_summary():
    """Get a summary of current configuration"""
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "openai_model": OPENAI_MODEL,
        "openai_max_tokens": OPENAI_MAX_TOKENS,
        "openai_temperature": OPENAI_TEMPERATURE,
        "request_timeout": REQUEST_TIMEOUT,
        "max_content_length": MAX_CONTENT_LENGTH,
        "streamlit_port": STREAMLIT_SERVER_PORT,
        "api_key_configured": OPENAI_API_KEY != "your_openai_api_key_here"
    } 