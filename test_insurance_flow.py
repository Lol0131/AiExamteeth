#!/usr/bin/env python3
"""
Test script to demonstrate the insurance pricing workflow
"""
import json
import uuid
import os

def create_test_patient():
    """Create a test patient with findings for the insurance demo"""
    patient_id = str(uuid.uuid4())[:8]
    
    # Create test findings
    test_findings = [
        {
            "tooth_id": 14,
            "region": "MO",
            "conf": 0.85,
            "bbox": [200, 150, 250, 200],
            "cls": "caries"
        },
        {
            "tooth_id": 19,
            "region": "DO", 
            "conf": 0.92,
            "bbox": [300, 180, 350, 230],
            "cls": "caries"
        }
    ]
    
    # Save patient data
    patient_data = {
        "patient_id": patient_id,
        "patient_name": "Test Patient",
        "findings": test_findings,
        "report": "AI detected potential cavities in teeth #14 and #19. Treatment may be needed.",
        "overlay_path": ".outputs/test_overlay.png"
    }
    
    os.makedirs(".outputs", exist_ok=True)
    with open(f'.outputs/patient_{patient_id}.json', 'w') as f:
        json.dump(patient_data, f, indent=2)
    
    return patient_id

def show_insurance_demo():
    """Show how to test the insurance pricing workflow"""
    print("🏥 Insurance Pricing Demo - Step by Step")
    print("=" * 50)
    
    patient_id = create_test_patient()
    
    print(f"\n✅ Test patient created with ID: {patient_id}")
    print(f"🔗 Patient Portal: http://127.0.0.1:8080/patient/{patient_id}")
    
    print("\n📋 DEMO STEPS:")
    print("1. Open the patient portal link above")
    print("2. In the chat, type one of these pricing questions:")
    print("   • 'How much will this cost?'")
    print("   • 'What's the price for treatment?'")
    print("   • 'Is this expensive?'")
    print("   • 'Can I afford this?'")
    print("   • 'What does insurance cover?'")
    
    print("\n3. The AI will show an insurance consent form")
    print("4. Fill in the form with fake data:")
    print("   • Insurance Provider: Blue Cross Blue Shield")
    print("   • Plan Type: Standard (80% coverage)")
    print("   • Deductible: $500")
    
    print("\n5. Click 'Yes, Calculate My Costs'")
    print("6. See the pricing breakdown")
    print("7. Try 'Find Other Doctors' to see the doctor network")
    
    print("\n🎯 EXPECTED RESULTS:")
    print("• Insurance consent modal appears")
    print("• Pricing breakdown shows costs for different treatments")
    print("• Doctor network shows 4 alternative providers")
    print("• All with realistic fake data for demonstration")
    
    print(f"\n🚀 Ready to test! Patient ID: {patient_id}")

if __name__ == "__main__":
    show_insurance_demo()
