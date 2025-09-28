#!/usr/bin/env python3
"""
Test SMS functionality
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_sms_setup():
    """Test if SMS credentials are properly configured"""
    print("📱 Testing SMS Setup...")
    print("=" * 40)
    
    # Check credentials
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    phone_number = os.getenv("TWILIO_PHONE_NUMBER")
    
    print(f"✅ Twilio Account SID: {'Found' if account_sid else 'Not found'}")
    print(f"✅ Twilio Auth Token: {'Found' if auth_token else 'Not found'}")
    print(f"✅ Twilio Phone Number: {'Found' if phone_number else 'Not found'}")
    
    if account_sid and auth_token and phone_number:
        print("\n🎉 SMS is ready to use!")
        print("📱 Patients will now receive text messages with their results")
        print("🔗 Messages include direct links to their personalized portal")
        print("💬 Patients can chat with AI about their specific findings")
        
        print(f"\n📞 Your Twilio Phone Number: {phone_number}")
        print("📱 Test by uploading an X-ray and checking 'Send SMS'")
        
    else:
        print("\n⚠️ SMS credentials not fully configured")
        print("Add these to your .env file:")
        print("TWILIO_ACCOUNT_SID=your-account-sid")
        print("TWILIO_AUTH_TOKEN=your-auth-token")
        print("TWILIO_PHONE_NUMBER=+1234567890")

if __name__ == "__main__":
    test_sms_setup()
