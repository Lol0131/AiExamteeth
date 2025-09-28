#!/usr/bin/env python3
"""
Working dental app with stable Gradio 3.50.2
"""
import json, os
import gradio as gr
from src.detect import Detector
from src.tooth_numbering import grid_tooth_map
from src.postprocess import assign_lesions_to_teeth_and_format

# Initialize detector
detector = Detector()
os.makedirs(".outputs", exist_ok=True)

def analyze_xray(img):
    """Analyze X-ray and return results"""
    if img is None:
        return None, "Please upload an X-ray image"
    
    try:
        # Detection and processing
        dets = detector.detect(img)
        locator = grid_tooth_map(img.size, "universal")
        findings, overlay = assign_lesions_to_teeth_and_format(img, dets, locator)
        
        # Generate report
        if not findings:
            report = "✅ No cavities detected - your teeth look healthy!"
        else:
            report = "🔍 Cavity Detection Results:\n"
            for finding in findings:
                report += f"• Tooth #{finding['tooth_id']} ({finding['region']}) - Confidence: {finding['conf']:.2f}\n"
        
        # Save results
        out = {"findings": findings}
        with open(".outputs/last_result.json", "w") as f:
            json.dump(out, f, indent=2)
        
        return overlay, report
    
    except Exception as e:
        error_msg = f"Error processing image: {str(e)}"
        return None, error_msg

# Create the interface
def create_app():
    return gr.Interface(
        fn=analyze_xray,
        inputs=gr.Image(type="pil", label="Upload dental X-ray"),
        outputs=[
            gr.Image(type="pil", label="Detection Overlay"),
            gr.Textbox(label="Results", lines=5)
        ],
        title="🦷 AI Dental Exam - Cavity Detection",
        description="**Prototype Demo - Not for clinical use**\n\nUpload an X-ray to detect cavities.",
        allow_flagging="never"
    )

if __name__ == "__main__":
    print("🚀 Starting AI Dental Exam app...")
    app = create_app()
    print("✅ Interface created successfully!")
    print("🌐 Launching on http://127.0.0.1:8000")
    app.launch(share=True, server_name="0.0.0.0", server_port=8000)