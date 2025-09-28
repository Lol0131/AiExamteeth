#!/usr/bin/env python3
"""
Demo the new personalized welcome message
"""
import json

def demo_welcome_message():
    """Show what the new welcome message looks like"""
    print("👋 Patient Portal Welcome Message Demo")
    print("=" * 50)
    
    # Example patient data
    patient_name = "Paula"
    patient_age = "35"
    insurance_provider = "blue_cross"
    
    # Example findings
    findings = [
        {"tooth_id": 14, "region": "MO", "conf": 0.85, "cls": "caries"},
        {"tooth_id": 19, "region": "DO", "conf": 0.72, "cls": "caries"}
    ]
    
    print(f"👋 Hi {patient_name}! Welcome to your personalized dental portal.")
    print("\n📋 **Today's Visit Summary:**")
    print(f"• AI analysis detected {len(findings)} potential issues")
    for finding in findings:
        confidence = finding["conf"]
        confidence_text = "High" if confidence > 0.8 else "Medium" if confidence > 0.6 else "Low"
        print(f"  - Tooth #{finding['tooth_id']} ({confidence_text} confidence: {confidence*100:.0f}%)")
    
    print("\n💡 **Next Steps:** I can help you understand your results, discuss treatment options, and provide cost estimates based on your insurance.")
    print(f"\n👤 **Your Information:** Age {patient_age}, Insurance: {insurance_provider.replace('_', ' ').title()}")
    
    print("\n💬 **How can I help you today?** You can ask me about:")
    print("• Treatment options and costs")
    print("• Insurance coverage details") 
    print("• Finding alternative providers")
    print("• General dental health questions")
    
    print("\n🎯 Key Features:")
    print("✅ Personalized greeting with patient name")
    print("✅ Visit summary with findings")
    print("✅ Confidence levels for each detection")
    print("✅ Patient context (age, insurance)")
    print("✅ Clear next steps and help options")
    print("✅ Professional medical presentation")

if __name__ == "__main__":
    demo_welcome_message()
