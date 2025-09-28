#!/usr/bin/env python3
"""
Setup script for OpenAI API key configuration
"""
import os

def setup_openai_key():
    """Help user set up OpenAI API key"""
    print("🔑 OpenAI API Key Setup")
    print("=" * 40)
    
    # Check if key is already set
    current_key = os.getenv("OPENAI_API_KEY")
    if current_key:
        print(f"✅ OpenAI API key is already set: {current_key[:8]}...")
        return True
    
    print("To use the AI chatbot, you need to set up your OpenAI API key.")
    print("\n📋 Steps:")
    print("1. Go to https://platform.openai.com/api-keys")
    print("2. Create a new API key")
    print("3. Copy the key")
    print("4. Set it as an environment variable")
    
    print("\n🔧 How to set the environment variable:")
    print("\nFor macOS/Linux (add to ~/.bashrc or ~/.zshrc):")
    print("export OPENAI_API_KEY='your-api-key-here'")
    
    print("\nFor Windows (Command Prompt):")
    print("set OPENAI_API_KEY=your-api-key-here")
    
    print("\nFor Windows (PowerShell):")
    print("$env:OPENAI_API_KEY='your-api-key-here'")
    
    print("\nOr you can set it temporarily for this session:")
    api_key = input("\nEnter your OpenAI API key (or press Enter to skip): ").strip()
    
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        print("✅ API key set for this session!")
        print("💡 To make it permanent, add it to your shell profile.")
        return True
    else:
        print("⚠️ No API key provided. The chatbot will use fallback responses.")
        return False

if __name__ == "__main__":
    setup_openai_key()
