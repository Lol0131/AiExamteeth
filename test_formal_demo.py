#!/usr/bin/env python3
"""
Demo the new formal welcome message
"""
import json

def demo_formal_welcome():
    """Show what the new formal welcome message looks like"""
    print("🏥 Formal Dental Portal Welcome Message Demo")
    print("=" * 60)
    
    # Example patient data
    patient_name = "Paula"
    patient_age = "35"
    insurance_provider = "blue_cross"
    
    # Example findings
    findings = [
        {"tooth_id": 14, "region": "MO", "conf": 0.85, "cls": "caries"},
        {"tooth_id": 19, "region": "DO", "conf": 0.72, "cls": "caries"}
    ]
    
    print(f"Hello {patient_name}, welcome to your dental analysis portal.")
    print("\n**Clinical Analysis Summary:**")
    print(f"AI analysis has identified {len(findings)} potential dental issues requiring attention:")
    for finding in findings:
        confidence = finding["conf"]
        confidence_text = "High" if confidence > 0.8 else "Medium" if confidence > 0.6 else "Low"
        print(f"- Tooth #{finding['tooth_id']} ({confidence_text} confidence: {confidence*100:.0f}%)")
    
    print("\n**Recommended Actions:** I can assist you with understanding your results, discussing treatment options, and providing cost estimates based on your insurance coverage.")
    print(f"\n**Patient Information:** Age {patient_age}, Insurance Provider: {insurance_provider.replace('_', ' ').title()}")
    
    print("\n**How may I assist you today?** You can inquire about:")
    print("• Treatment options and associated costs")
    print("• Insurance coverage and benefits")
    print("• Alternative provider options")
    print("• General dental health information")
    
    print("\n🎯 Key Changes:")
    print("✅ Removed all emojis for professional appearance")
    print("✅ Formal medical terminology")
    print("✅ Clinical language and structure")
    print("✅ Professional tone throughout")
    print("✅ Medical-grade presentation")
    
    print("\n📋 Style Comparison:")
    print("BEFORE: 👋 Hi Paula! Welcome to your personalized dental portal.")
    print("AFTER:  Hello Paula, welcome to your dental analysis portal.")
    print()
    print("BEFORE: 📋 Today's Visit Summary:")
    print("AFTER:  **Clinical Analysis Summary:**")
    print()
    print("BEFORE: 💡 Next Steps:")
    print("AFTER:  **Recommended Actions:**")

if __name__ == "__main__":
    demo_formal_welcome()
