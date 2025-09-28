#!/usr/bin/env python3
"""
Test the complete doctor-to-patient workflow
"""
import json
import uuid
import os

def create_demo_patient():
    """Create a demo patient with comprehensive information"""
    patient_id = str(uuid.uuid4())[:8]
    
    # Create comprehensive patient data
    patient_data = {
        "patient_id": patient_id,
        "patient_name": "John Smith",
        "patient_age": "35",
        "patient_email": "john.smith@email.com",
        "patient_phone": "(555) 123-4567",
        "patient_history": "Diabetes, takes metformin",
        "insurance_provider": "blue_cross",
        "findings": [
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
        ],
        "report": "AI detected potential cavities in teeth #14 and #19. Given your diabetes history, these findings require special attention and prompt treatment.",
        "overlay_path": ".outputs/demo_overlay.png"
    }
    
    os.makedirs(".outputs", exist_ok=True)
    with open(f'.outputs/patient_{patient_id}.json', 'w') as f:
        json.dump(patient_data, f, indent=2)
    
    return patient_id, patient_data

def show_complete_demo():
    """Show the complete workflow demonstration"""
    print("🦷 Complete AI Dental Exam Demo")
    print("=" * 50)
    
    patient_id, patient_data = create_demo_patient()
    
    print(f"\n✅ Demo patient created with ID: {patient_id}")
    print(f"👤 Patient: {patient_data['patient_name']} (Age: {patient_data['patient_age']})")
    print(f"📧 Email: {patient_data['patient_email']}")
    print(f"📞 Phone: {patient_data['patient_phone']}")
    print(f"🏥 Medical History: {patient_data['patient_history']}")
    print(f"💳 Insurance: {patient_data['insurance_provider'].replace('_', ' ').title()}")
    
    print(f"\n🔗 Patient Portal: http://127.0.0.1:8080/patient/{patient_id}")
    print(f"👨‍⚕️ Doctor Interface: http://127.0.0.1:8080")
    
    print("\n📋 COMPLETE WORKFLOW:")
    print("1. 👨‍⚕️ DOCTOR SIDE:")
    print("   - Go to: http://127.0.0.1:8080")
    print("   - Upload X-ray image")
    print("   - Fill comprehensive patient form:")
    print("     • Name: John Smith")
    print("     • Age: 35")
    print("     • Email: john.smith@email.com")
    print("     • Phone: (555) 123-4567")
    print("     • Medical History: Diabetes, takes metformin")
    print("     • Insurance: Blue Cross Blue Shield")
    print("     • ☑️ Send email")
    print("   - Click 'Analyze X-ray'")
    print("   - Get patient ID and portal link")
    
    print("\n2. 👤 PATIENT SIDE:")
    print("   - Patient receives personalized email")
    print("   - Clicks link to patient portal")
    print("   - Sees personalized information display")
    print("   - Tests personalized AI chat:")
    print("     • 'Hello' → AI responds with 'Hello John!'")
    print("     • 'What do my results mean?' → AI references specific findings")
    print("     • 'How much will this cost?' → Insurance pricing modal")
    print("     • 'What treatments do I need?' → Personalized treatment advice")
    
    print("\n🎯 PERSONALIZED FEATURES:")
    print("✅ AI addresses patient by name")
    print("✅ References specific tooth findings")
    print("✅ Considers diabetes medical history")
    print("✅ Insurance pricing based on Blue Cross Blue Shield")
    print("✅ Personalized treatment recommendations")
    print("✅ Complete doctor-to-patient workflow")
    
    print(f"\n🚀 Ready to test! Patient ID: {patient_id}")

if __name__ == "__main__":
    show_complete_demo()
