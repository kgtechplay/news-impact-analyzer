"""
Configuration settings for News Impact Analyzer
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_MAX_TOKENS = 1000
OPENAI_TEMPERATURE = 0.3

# Web Scraping Configuration
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
REQUEST_TIMEOUT = 10
MAX_CONTENT_LENGTH = 4000  # Maximum characters to send to OpenAI API

# Streamlit Configuration
PAGE_TITLE = "News Impact Analyzer"
PAGE_ICON = "📊"
LAYOUT = "wide"

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