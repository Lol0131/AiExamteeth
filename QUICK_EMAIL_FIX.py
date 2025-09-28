#!/usr/bin/env python3
"""
Quick fix for email authentication issues
Run this script to disable email for demo purposes
"""

import os

def create_demo_env():
    """Create a .env file that disables email for demo"""
    env_content = """# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Email Configuration (DISABLED for demo)
EMAIL_USERNAME=
EMAIL_PASSWORD=
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587

# SMS Configuration (Twilio)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file with email disabled")
    print("📧 Email functionality is now disabled for demo")
    print("🔗 Patient portal links will still be generated")
    print("📱 SMS functionality can still be configured if needed")

if __name__ == "__main__":
    create_demo_env()
