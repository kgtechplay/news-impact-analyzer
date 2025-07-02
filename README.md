# News Impact Analyzer

A Streamlit application that analyzes web content to identify Indian companies that could be impacted by news articles and provides detailed impact analysis.

## Features

- 🔗 **Web Content Scraping**: Automatically extracts content from any web URL
- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT to analyze content and identify impacted companies
- 🇮🇳 **Indian Market Focus**: Specifically identifies Indian companies and their market listings
- 📊 **Structured Output**: Provides results in JSON format with impact scores and industry classification
- 📥 **Export Functionality**: Download results as JSON files

## Output Format

The application provides analysis results in the following JSON format:

```json
[
    {
        "company name": "Tata Motors",
        "impact type": "positive",
        "company industry": "Automotive",
        "impact score": 7,
        "listed": "Y"
    }
]
```

### Field Descriptions

- **company name**: Exact name of the Indian company
- **impact type**: "positive" or "negative" based on news impact
- **company industry**: Industry sector the company operates in
- **impact score**: Score from 0-10 (10 being highest impact)
- **listed**: "Y" if listed on BSE/NSE, "N" if not

## Setup Instructions

### 1. Install Dependencies

```bash
python setup.py
```

This will automatically install all required packages and create the environment file.

### 2. Configure Environment Variables (Optional)

The application will prompt you for your OpenAI API key through the UI when you first run it. However, you can also set it in the `.env` file for convenience.

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Either:
   - Enter it in the UI when prompted (recommended), or
   - Edit the `.env` file and replace `your_openai_api_key_here` with your actual API key

**Optional:** You can also customize other settings in the `.env` file:
- `OPENAI_MODEL`: AI model to use (default: gpt-3.5-turbo)
- `OPENAI_MAX_TOKENS`: Maximum tokens for API calls (default: 1000)
- `OPENAI_TEMPERATURE`: AI response randomness (default: 0.3)
- `REQUEST_TIMEOUT`: Web scraping timeout (default: 10 seconds)
- `MAX_CONTENT_LENGTH`: Maximum content length for analysis (default: 4000)
- `STREAMLIT_SERVER_PORT`: Port for Streamlit server (default: 8501)

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

1. **API Key Setup**: Enter your OpenAI API key when prompted (first time only)
2. **Enter URL**: Paste any news article or webpage URL in the input field
3. **Analyze**: Click the "Analyze Impact" button
4. **Review Results**: View the identified companies and their impact analysis
5. **Export**: Download results as JSON file if needed

**Note**: Your API key is stored securely in the session and can be changed anytime using the sidebar option.

## Example Use Cases

- Analyzing news articles for investment opportunities
- Monitoring market sentiment for specific industries
- Identifying companies affected by policy changes
- Researching competitive landscape impacts

## Configuration Management

Use the configuration manager to view and manage your settings:

```bash
python config_manager.py
```

This provides options to:
- View current configuration
- Show environment template
- Validate configuration
- Export configuration settings

## Technical Details

- **Web Scraping**: Uses BeautifulSoup for content extraction
- **AI Analysis**: OpenAI GPT-3.5-turbo for content analysis
- **Frontend**: Streamlit for user interface
- **Data Processing**: Pandas for data manipulation
- **Configuration**: Centralized environment management with `.env` file

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for web scraping and API calls

## Troubleshooting

- **API Key Issues**: Use `python config_manager.py` to validate your configuration
- **Web Scraping Errors**: Some websites may block automated access
- **Content Length**: Very long articles may be truncated for API efficiency
- **Configuration Issues**: Run `python test_app.py` to test all components

## License

This project is for educational and research purposes. 