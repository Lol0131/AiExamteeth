#!/usr/bin/env python3
"""
Demo the new pricing system based on actual findings
"""
import json

def demo_pricing_system():
    """Demonstrate how pricing now works based on actual findings"""
    print("🦷 Dental Pricing System Demo")
    print("=" * 50)
    
    # Example findings from AI detection
    example_findings = [
        {"tooth_id": 14, "region": "MO", "conf": 0.85, "cls": "caries"},
        {"tooth_id": 19, "region": "DO", "conf": 0.72, "cls": "caries"},
        {"tooth_id": 30, "region": "O", "conf": 0.45, "cls": "caries"}
    ]
    
    print("📊 Example AI Detection Results:")
    for finding in example_findings:
        confidence_level = "High" if finding["conf"] > 0.8 else "Medium" if finding["conf"] > 0.6 else "Low"
        print(f"  • Tooth #{finding['tooth_id']} - {confidence_level} confidence ({finding['conf']:.2f})")
    
    print("\n💰 Treatment Recommendations Based on Findings:")
    
    # Simulate the pricing logic
    for finding in example_findings:
        confidence = finding["conf"]
        tooth_id = finding["tooth_id"]
        
        # Determine treatment based on confidence
        if confidence > 0.8:
            treatment = "Crown" if confidence > 0.85 else "Root Canal"
            cost = 1200 if treatment == "Crown" else 800
        elif confidence > 0.6:
            treatment = "Filling"
            cost = 150
        else:
            treatment = "Extraction"
            cost = 200
            
        print(f"  • Tooth #{tooth_id}: {treatment} (${cost}) - {confidence:.2f} confidence")
    
    print("\n🎯 Key Improvements:")
    print("  ✅ Pricing based on ACTUAL detected cavities")
    print("  ✅ Different treatments for different confidence levels")
    print("  ✅ Tooth-specific recommendations")
    print("  ✅ No more generic 'You Pay: $502' for everything")
    print("  ✅ Shows confidence levels and descriptions")
    print("  ✅ Calculates realistic totals")
    
    print("\n📱 How to Test:")
    print("  1. Upload an X-ray with cavities")
    print("  2. Go to patient portal")
    print("  3. Ask about pricing in chat")
    print("  4. See personalized treatment costs!")

if __name__ == "__main__":
    demo_pricing_system()
