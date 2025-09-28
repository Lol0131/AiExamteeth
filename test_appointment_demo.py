#!/usr/bin/env python3
"""
Demo the new appointment booking system
"""
import json

def demo_appointment_booking():
    """Show what the new appointment booking looks like"""
    print("📅 Doctor Network with Appointment Booking Demo")
    print("=" * 60)
    
    # Example doctors with appointment slots
    doctors = [
        {
            "name": "Dr. Sarah Johnson",
            "specialty": "General Dentistry", 
            "rating": "⭐⭐⭐⭐⭐",
            "price": "$1,200",
            "location": "Downtown Clinic",
            "distance": "2.3 miles",
            "appointments": [
                {"date": "Tomorrow", "time": "2:00 PM", "type": "Consultation"},
                {"date": "Friday", "time": "10:30 AM", "type": "Treatment"},
                {"date": "Next Monday", "time": "3:15 PM", "type": "Consultation"}
            ]
        },
        {
            "name": "Dr. Michael Chen",
            "specialty": "Restorative Dentistry",
            "rating": "⭐⭐⭐⭐", 
            "price": "$1,100",
            "location": "Westside Dental",
            "distance": "3.1 miles",
            "appointments": [
                {"date": "Today", "time": "4:00 PM", "type": "Emergency"},
                {"date": "Thursday", "time": "11:00 AM", "type": "Consultation"},
                {"date": "Next Tuesday", "time": "2:30 PM", "type": "Treatment"}
            ]
        }
    ]
    
    print("🦷 Available Doctors with Appointment Slots:")
    print()
    
    for doctor in doctors:
        print(f"👨‍⚕️ {doctor['name']}")
        print(f"   Specialty: {doctor['specialty']}")
        print(f"   Location: {doctor['location']} ({doctor['distance']} away)")
        print(f"   Rating: {doctor['rating']}")
        print(f"   Your Cost: {doctor['price']}")
        print()
        print("   📅 Available Appointments:")
        for apt in doctor['appointments']:
            print(f"      • {apt['date']} at {apt['time']} ({apt['type']})")
        print()
    
    print("🎯 New Features:")
    print("✅ Real appointment slots with dates and times")
    print("✅ Different appointment types (Consultation, Treatment, Emergency)")
    print("✅ One-click booking with 'Book Now' buttons")
    print("✅ Booking confirmation with all details")
    print("✅ SMS confirmation notification")
    print("✅ Professional medical presentation")
    
    print("\n📱 How It Works:")
    print("1. Patient asks about pricing")
    print("2. AI shows insurance pricing")
    print("3. If patient doesn't like price, AI offers doctor network")
    print("4. Patient sees available doctors with appointment slots")
    print("5. Patient clicks 'Book Now' for preferred slot")
    print("6. Patient gets confirmation and SMS notification")
    
    print("\n💬 Example Booking Confirmation:")
    print("📅 Appointment Booked!")
    print("Doctor: Dr. Sarah Johnson")
    print("Date: Tomorrow")
    print("Time: 2:00 PM")
    print("Type: Consultation")
    print("Cost: $1,200")
    print("✅ You'll receive a confirmation text message shortly.")
    print("📱 The doctor's office will contact you to confirm details.")

if __name__ == "__main__":
    demo_appointment_booking()
