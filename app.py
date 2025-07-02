import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
from openai import OpenAI
import os
import re
import pandas as pd
from environment import *

def scrape_webpage(url):
    """Scrape content from a webpage"""
    try:
        headers = {
            'User-Agent': USER_AGENT
        }
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text[:MAX_CONTENT_LENGTH]  # Limit content length for API efficiency
    except Exception as e:
        st.error(f"Error scraping webpage: {str(e)}")
        return None

def analyze_content_with_llm(content, api_key):
    """Analyze content using OpenAI to identify impacted Indian companies"""
    
    # Create OpenAI client with provided key
    client = OpenAI(api_key=api_key)
    
    prompt = DEFAULT_PROMPT_TEMPLATE.format(content=content)
    
    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a financial analyst specializing in Indian markets and company analysis."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=OPENAI_MAX_TOKENS,
            temperature=OPENAI_TEMPERATURE
        )
        
        result = response.choices[0].message.content
        if result:
            result = result.strip()
        
        # Extract JSON from the response
        if result:
            json_match = re.search(r'\[.*\]', result, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            else:
                st.error("Could not parse LLM response as JSON")
                return []
        else:
            st.error("Empty response from OpenAI API")
            return []
            
    except Exception as e:
        st.error(f"Error calling OpenAI API: {str(e)}")
        return []

def validate_api_key(api_key):
    """Validate OpenAI API key by making a simple test call"""
    try:
        client = OpenAI(api_key=api_key)
        # Make a minimal test call
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        return True
    except Exception as e:
        print(f"API Key validation error: {str(e)}")  # Debug print
        return False

def main():
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout="wide" if LAYOUT == "wide" else "centered"
    )
    
    # Initialize session state
    if 'api_key_validated' not in st.session_state:
        st.session_state.api_key_validated = False
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""
    
    # API Key Input Section
    if not st.session_state.api_key_validated:
        st.title("🔑 OpenAI API Key Setup")
        st.markdown("Please enter your OpenAI API key to get started")
        
        with st.form("api_key_form"):
            api_key = st.text_input(
                "OpenAI API Key:",
                type="password",
                placeholder="sk-...",
                help="Enter your OpenAI API key. Get it from https://platform.openai.com/api-keys"
            )
            
            col1, col2 = st.columns([1, 1])
            with col1:
                submit_button = st.form_submit_button("🔍 Validate Key", type="primary")
            with col2:
                if st.form_submit_button("ℹ️ Get API Key"):
                    st.info("""
                    **How to get your OpenAI API key:**
                    1. Go to https://platform.openai.com/api-keys
                    2. Sign in or create an account
                    3. Click "Create new secret key"
                    4. Copy the key (starts with 'sk-')
                    5. Paste it in the field above
                    """)
        
        if submit_button and api_key:
            with st.spinner("🔍 Validating API key..."):
                if validate_api_key(api_key):
                    st.session_state.api_key = api_key
                    st.session_state.api_key_validated = True
                    st.success("✅ API key validated successfully!")
                    st.rerun()
                else:
                    st.error("❌ Invalid API key. Please check and try again.")
        
        # Show help if no key entered
        if not api_key:
            st.info("💡 **Need an API key?** Click 'Get API Key' for instructions.")
        
        return
    
    # Main Application (after API key validation)
    st.title("📊 News Impact Analyzer")
    st.markdown("Analyze web content to identify Indian companies that could be impacted by news")
    
    # API Key Status
    with st.sidebar:
        st.header("🔑 API Status")
        st.success("✅ API Key Validated")
        if st.button("🔄 Change API Key"):
            st.session_state.api_key_validated = False
            st.session_state.api_key = ""
            st.rerun()
    
    # Input section
    st.header("🔗 Enter Web Link")
    url = st.text_input(
        "Paste the web link here:",
        placeholder="https://example.com/news-article",
        help="Enter a valid URL to analyze the content"
    )
    
    # Analyze button
    if st.button("🚀 Analyze Impact", type="primary"):
        if not url:
            st.warning("Please enter a valid URL")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        with st.spinner("🔍 Scraping webpage..."):
            content = scrape_webpage(url)
        
        if content:
            st.success("✅ Webpage content retrieved successfully!")
            
            # Display content preview
            with st.expander("📄 Content Preview"):
                st.text(content[:500] + "..." if len(content) > 500 else content)
            
            with st.spinner("🤖 Analyzing content with AI..."):
                results = analyze_content_with_llm(content, st.session_state.api_key)
            
            if results:
                st.success(f"✅ Analysis complete! Found {len(results)} impacted companies")
                
                # Display results
                st.header("📈 Impact Analysis Results")
                
                # Create a DataFrame for better display
                df = pd.DataFrame(results)
                
                # Display as table
                st.dataframe(df, use_container_width=True)
                
                # Display JSON
                st.subheader("📋 JSON Output")
                st.json(results)
                
                # Download button
                st.download_button(
                    label="📥 Download Results as JSON",
                    data=json.dumps(results, indent=2),
                    file_name="impact_analysis_results.json",
                    mime="application/json"
                )
                
            else:
                st.info("ℹ️ No relevant Indian companies found in the analyzed content")
        else:
            st.error("❌ Failed to retrieve webpage content")

if __name__ == "__main__":
    main() 