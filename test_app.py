"""
Test script for News Impact Analyzer functionality
Run this to test the core functions without Streamlit
"""

import os
from environment import validate_config, get_config_summary, OPENAI_API_KEY
from app import scrape_webpage, analyze_content_with_llm, validate_api_key

def test_scraping():
    """Test web scraping functionality"""
    print("Testing web scraping...")
    
    # Test with a sample news URL
    test_url = "https://economictimes.indiatimes.com/news/economy/policy"
    
    try:
        content = scrape_webpage(test_url)
        if content:
            print("✅ Web scraping successful!")
            print(f"Content length: {len(content)} characters")
            print("First 200 characters:")
            print(content[:200] + "...")
            return content
        else:
            print("❌ Web scraping failed")
            return None
    except Exception as e:
        print(f"❌ Error during scraping: {e}")
        return None

def test_llm_analysis(content):
    """Test LLM analysis functionality"""
    print("\nTesting LLM analysis...")
    
    if not validate_config():
        print("❌ OpenAI API key not found. Please set OPENAI_API_KEY in .env file")
        return None
    
    try:
        results = analyze_content_with_llm(content, OPENAI_API_KEY)
        if results:
            print("✅ LLM analysis successful!")
            print(f"Found {len(results)} companies")
            print("Results:")
            for company in results:
                print(f"- {company['company name']}: {company['impact type']} impact (score: {company['impact score']})")
        else:
            print("ℹ️ No companies found in analysis")
        return results
    except Exception as e:
        print(f"❌ Error during LLM analysis: {e}")
        return None

def main():
    print("🧪 Testing News Impact Analyzer Components\n")
    
    # Show configuration summary
    config = get_config_summary()
    print("📋 Configuration Summary:")
    print(f"   App: {config['app_name']} v{config['app_version']}")
    print(f"   OpenAI Model: {config['openai_model']}")
    print(f"   API Key Configured: {'✅' if config['api_key_configured'] else '❌'}")
    print()
    
    # Test web scraping
    content = test_scraping()
    
    if content:
        # Test LLM analysis
        results = test_llm_analysis(content)
        
        if results:
            print("\n✅ All tests passed! The application is ready to use.")
        else:
            print("\n⚠️ LLM analysis failed. Check your OpenAI API key.")
    else:
        print("\n❌ Web scraping failed. Check your internet connection.")

if __name__ == "__main__":
    main() 