#!/usr/bin/env python3
"""
Demo script to test the complete doctor → patient workflow
"""
import json
import uuid
import os

def create_demo_patient_data():
    """Create demo patient data for testing"""
    patient_id = str(uuid.uuid4())[:8]
    
    # Simulate AI analysis results
    demo_findings = [
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
    
    demo_report = """🔍 Cavity Detection Results:
• Tooth #14 - Confidence: 0.85
• Tooth #19 - Confidence: 0.92

The AI has detected potential cavities in two teeth. Please schedule a follow-up appointment to discuss treatment options."""
    
    # Save patient data
    patient_data = {
        "patient_id": patient_id,
        "patient_name": "Demo Patient",
        "findings": demo_findings,
        "report": demo_report,
        "overlay_path": ".outputs/demo_overlay.png"
    }
    
    os.makedirs(".outputs", exist_ok=True)
    with open(f'.outputs/patient_{patient_id}.json', 'w') as f:
        json.dump(patient_data, f, indent=2)
    
    print(f"✅ Demo patient data created!")
    print(f"📋 Patient ID: {patient_id}")
    print(f"🔗 Patient Portal: http://127.0.0.1:8080/patient/{patient_id}")
    print(f"📧 Email would contain: 'Click here to view your results: http://127.0.0.1:8080/patient/{patient_id}'")
    
    return patient_id

def show_workflow():
    """Show the complete workflow"""
    print("🦷 AI Dental Exam - Complete Workflow Demo")
    print("=" * 50)
    
    print("\n👨‍⚕️ DOCTOR SIDE:")
    print("1. Doctor goes to: http://127.0.0.1:8080")
    print("2. Uploads X-ray image")
    print("3. Fills patient form:")
    print("   - Name: Demo Patient")
    print("   - Email: demo@example.com")
    print("   - ☑️ Send email")
    print("4. Clicks 'Analyze X-ray'")
    print("5. AI detects cavities and creates overlay")
    print("6. System generates patient ID and sends email")
    
    print("\n👤 PATIENT SIDE:")
    print("1. Patient receives email with link")
    print("2. Patient clicks link to view results")
    print("3. Patient sees their specific findings")
    print("4. Patient chats with AI about their results")
    
    print("\n💬 AI CHAT EXAMPLES:")
    print("- 'What does this finding mean?'")
    print("- 'What treatments might I need?'")
    print("- 'How serious are these cavities?'")
    print("- 'What can I do to prevent more issues?'")
    
    print("\n🚀 TESTING STEPS:")
    print("1. Start Flask app: python3 flask_app.py")
    print("2. Open doctor interface: http://127.0.0.1:8080")
    print("3. Upload X-ray and fill patient form")
    print("4. Note the patient ID generated")
    print("5. Open patient portal: http://127.0.0.1:8080/patient/<patient_id>")
    print("6. Test the AI chat feature")

if __name__ == "__main__":
    show_workflow()
    print("\n" + "=" * 50)
    patient_id = create_demo_patient_data()
    print(f"\n🎯 Ready to test! Use patient ID: {patient_id}")
