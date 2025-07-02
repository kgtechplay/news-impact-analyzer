# News Impact Analyzer

A Streamlit application that analyzes web content to identify Indian companies that could be impacted by news articles and provides detailed impact analysis.

## 🌟 Features

- 🔗 **Web Content Scraping**: Automatically extracts content from any web URL
- 🤖 **AI-Powered Analysis**: Uses OpenAI GPT to analyze content and identify impacted companies
- 🇮🇳 **Indian Market Focus**: Specifically identifies Indian companies and their market listings
- 📊 **Structured Output**: Provides results in JSON format with impact scores and industry classification
- 📥 **Export Functionality**: Download results as JSON files
- 🔧 **Easy Setup**: Virtual environment and automated dependency management

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ (Tested with Python 3.13)
- OpenAI API key
- Internet connection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kgtechplay/news-impact-analyzer.git
   cd news-impact-analyzer
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows PowerShell
   # or
   source venv/bin/activate     # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r venv_requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📋 Setup Instructions

### 1. Install Dependencies

```bash
python setup.py
```

This will automatically install all required packages and create the environment file.

### 2. Configure OpenAI API Key

The application will prompt you for your OpenAI API key through the UI when you first run it. However, you can also set it in the `.env` file for convenience.

1. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Either:
   - Enter it in the UI when prompted (recommended), or
   - Edit the `.env` file and replace `your_openai_api_key_here` with your actual API key

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📊 Output Format

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

## 🛠️ Configuration

### Environment Variables

You can customize settings in the `.env` file:
- `OPENAI_MODEL`: AI model to use (default: gpt-3.5-turbo)
- `OPENAI_MAX_TOKENS`: Maximum tokens for API calls (default: 1000)
- `OPENAI_TEMPERATURE`: AI response randomness (default: 0.3)
- `REQUEST_TIMEOUT`: Web scraping timeout (default: 10 seconds)
- `MAX_CONTENT_LENGTH`: Maximum content length for analysis (default: 4000)
- `STREAMLIT_SERVER_PORT`: Port for Streamlit server (default: 8501)

### Configuration Management

Use the configuration manager to view and manage your settings:

```bash
python config_manager.py
```

## 🧪 Testing

### Test API Key
```bash
python test_api_key.py <your_api_key>
```

### Test Application Components
```bash
python test_app.py
```

## 📁 Project Structure

```
news-impact-analyzer/
├── app.py                 # Main Streamlit application
├── environment.py         # Environment configuration
├── config_manager.py      # Configuration management
├── test_app.py           # Application testing
├── test_api_key.py       # API key validation
├── setup.py              # Setup script
├── requirements.txt      # Basic requirements
├── venv_requirements.txt # Exact virtual environment packages
├── run_app.bat          # Windows batch file for easy startup
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## 🔧 Troubleshooting

### Common Issues

1. **API Key Issues**
   - Use `python test_api_key.py <your_key>` to validate
   - Check if you have sufficient credits in your OpenAI account
   - Verify your account is active at https://platform.openai.com/

2. **Web Scraping Errors**
   - Some websites may block automated access
   - Check your internet connection
   - Try different news sources

3. **Content Length Issues**
   - Very long articles may be truncated for API efficiency
   - This is normal and expected behavior

4. **Protobuf Version Issues**
   - If you encounter protobuf errors, the project uses `protobuf==3.20.3`
   - Run: `pip install protobuf==3.20.3`

### Getting Help

1. **Check the logs** in the Streamlit interface
2. **Run test scripts** to isolate issues
3. **Verify your setup** with `python test_app.py`

## 🎯 Example Use Cases

- Analyzing news articles for investment opportunities
- Monitoring market sentiment for specific industries
- Identifying companies affected by policy changes
- Researching competitive landscape impacts
- Due diligence for investment decisions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is for educational and research purposes.

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Streamlit for the web framework
- BeautifulSoup for web scraping capabilities

---

**Made with ❤️ for Indian market analysis** 