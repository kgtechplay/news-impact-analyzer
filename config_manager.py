"""
Configuration Manager for News Impact Analyzer
Helps manage environment variables and configuration settings
"""

import os
import json
from environment import validate_config, get_config_summary

def show_current_config():
    """Display current configuration"""
    config = get_config_summary()
    
    print("🔧 Current Configuration:")
    print("=" * 40)
    print(f"App Name: {config['app_name']}")
    print(f"App Version: {config['app_version']}")
    print(f"OpenAI Model: {config['openai_model']}")
    print(f"Max Tokens: {config['openai_max_tokens']}")
    print(f"Temperature: {config['openai_temperature']}")
    print(f"Request Timeout: {config['request_timeout']}s")
    print(f"Max Content Length: {config['max_content_length']} chars")
    print(f"Streamlit Port: {config['streamlit_port']}")
    print(f"API Key Configured: {'✅' if config['api_key_configured'] else '❌'}")
    print()

def show_env_template():
    """Show the environment file template"""
    print("📝 Environment File Template (.env):")
    print("=" * 40)
    print("""# OpenAI API Configuration
# Get your API key from: https://platform.openai.com/api-keys
OPENAI_API_KEY=your_openai_api_key_here

# Application Configuration
APP_NAME=News Impact Analyzer
APP_VERSION=1.0.0

# OpenAI Model Settings
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=1000
OPENAI_TEMPERATURE=0.3

# Web Scraping Settings
REQUEST_TIMEOUT=10
MAX_CONTENT_LENGTH=4000

# Streamlit Settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=localhost
""")

def validate_environment():
    """Validate environment configuration"""
    print("🔍 Validating Environment Configuration...")
    print("=" * 40)
    
    if validate_config():
        print("✅ Configuration is valid!")
        print("✅ OpenAI API key is configured")
        print("✅ All required settings are present")
    else:
        print("❌ Configuration issues found:")
        print("   - OpenAI API key not configured")
        print("   - Please set OPENAI_API_KEY in your .env file")
    
    print()

def export_config():
    """Export current configuration to JSON"""
    config = get_config_summary()
    
    # Remove sensitive information
    safe_config = config.copy()
    safe_config['api_key_configured'] = '***' if config['api_key_configured'] else 'Not Set'
    
    filename = "config_export.json"
    with open(filename, 'w') as f:
        json.dump(safe_config, f, indent=2)
    
    print(f"📤 Configuration exported to {filename}")
    print()

def main():
    print("⚙️  News Impact Analyzer - Configuration Manager")
    print("=" * 50)
    print()
    
    while True:
        print("Choose an option:")
        print("1. Show current configuration")
        print("2. Show environment template")
        print("3. Validate configuration")
        print("4. Export configuration")
        print("5. Exit")
        print()
        
        choice = input("Enter your choice (1-5): ").strip()
        print()
        
        if choice == "1":
            show_current_config()
        elif choice == "2":
            show_env_template()
        elif choice == "3":
            validate_environment()
        elif choice == "4":
            export_config()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.")
            print()

if __name__ == "__main__":
    main() 