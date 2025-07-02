"""
Demo script for News Impact Analyzer
Shows example usage and sample outputs
"""

import json
from datetime import datetime

def show_sample_output():
    """Display sample output format"""
    
    sample_data = [
        {
            "company name": "Tata Motors",
            "impact type": "positive",
            "company industry": "Automotive",
            "impact score": 7,
            "listed": "Y"
        },
        {
            "company name": "Maruti Suzuki",
            "impact type": "positive", 
            "company industry": "Automotive",
            "impact score": 6,
            "listed": "Y"
        },
        {
            "company name": "Mahindra & Mahindra",
            "impact type": "negative",
            "company industry": "Automotive",
            "impact score": 4,
            "listed": "Y"
        },
        {
            "company name": "Hero MotoCorp",
            "impact type": "positive",
            "company industry": "Two-Wheeler",
            "impact score": 5,
            "listed": "Y"
        }
    ]
    
    print("📊 Sample Analysis Output:")
    print("=" * 50)
    
    for company in sample_data:
        impact_emoji = "📈" if company["impact type"] == "positive" else "📉"
        listed_emoji = "🏢" if company["listed"] == "Y" else "🏭"
        
        print(f"{impact_emoji} {company['company name']}")
        print(f"   Industry: {company['company industry']}")
        print(f"   Impact: {company['impact type'].title()} (Score: {company['impact score']}/10)")
        print(f"   Listed: {listed_emoji} {company['listed']}")
        print()
    
    print("📋 JSON Format:")
    print(json.dumps(sample_data, indent=2))

def show_usage_instructions():
    """Display usage instructions"""
    
    print("🚀 How to Use News Impact Analyzer:")
    print("=" * 40)
    print()
    print("1. 📦 Install dependencies:")
    print("   python setup.py")
    print()
    print("2. 🔑 Configure OpenAI API:")
    print("   - Get API key from: https://platform.openai.com/api-keys")
    print("   - Add to .env file: OPENAI_API_KEY=your_key_here")
    print()
    print("3. 🌐 Run the application:")
    print("   streamlit run app.py")
    print()
    print("4. 🔗 Enter a news URL and analyze!")
    print()
    print("📝 Example URLs to test:")
    print("   - https://economictimes.indiatimes.com/news/economy/policy")
    print("   - https://www.moneycontrol.com/news/business/")
    print("   - https://www.livemint.com/market/")

def main():
    print("🎯 News Impact Analyzer Demo")
    print("=" * 30)
    print()
    
    show_sample_output()
    print()
    show_usage_instructions()
    
    print("\n" + "=" * 50)
    print(f"Demo generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main() 