#!/usr/bin/env python3
"""
Simple script to test OpenAI API key validation
"""

from openai import OpenAI
import sys

def test_api_key(api_key):
    """Test if the API key is valid"""
    try:
        print("🔍 Testing API key...")
        client = OpenAI(api_key=api_key)
        
        # Make a simple test call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello World'"}],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✅ API key is valid!")
        print(f"Response: {result}")
        return True
        
    except Exception as e:
        print(f"❌ API key validation failed: {str(e)}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_api_key.py <your_api_key>")
        print("Example: python test_api_key.py sk-1234567890abcdef...")
        sys.exit(1)
    
    api_key = sys.argv[1]
    
    # Basic format check
    if not api_key.startswith("sk-"):
        print("❌ Invalid API key format. API keys should start with 'sk-'")
        sys.exit(1)
    
    if len(api_key) < 20:
        print("❌ API key seems too short. Please check your key.")
        sys.exit(1)
    
    print(f"🔑 Testing API key: {api_key[:10]}...")
    
    if test_api_key(api_key):
        print("\n🎉 Your API key is working correctly!")
        print("You can now use it in the Streamlit application.")
    else:
        print("\n💡 Troubleshooting tips:")
        print("1. Make sure your API key is correct and complete")
        print("2. Check if you have sufficient credits in your OpenAI account")
        print("3. Verify your account is active at https://platform.openai.com/")
        print("4. Try generating a new API key if the issue persists")

if __name__ == "__main__":
    main() 