# app.py
import json, os
import gradio as gr
from src.detect import Detector
from src.tooth_numbering import grid_tooth_map
from src.postprocess import assign_lesions_to_teeth_and_format

detector = Detector()
os.makedirs(".outputs", exist_ok=True)

def run_pipeline(img, notation_system="universal"):
    if img is None:
        return None, "Upload an X-ray image", ""
    dets = detector.detect(img)
    locator = grid_tooth_map(img.size, notation_system)
    findings, overlay = assign_lesions_to_teeth_and_format(img, dets, locator)
    out = {"findings": findings}
    with open(".outputs/last_result.json", "w") as f:
        json.dump(out, f, indent=2)
    text = "No caries detected" if not findings else "\n".join(
        f"Tooth {r['tooth_id']} — {r['region']} caries (p={r['conf']:.2f})" for r in findings
    )
    return overlay, text, json.dumps(out, indent=2)

demo = gr.Interface(
    fn=run_pipeline,
    inputs=[gr.Image(type="pil", label="Upload dental X-ray"),
            gr.Radio(["universal","fdi"], value="universal", label="Notation")],
    outputs=[gr.Image(type="pil", label="Annotated"),
             gr.Textbox(label="Dentist-style output"),
             gr.Code(label="JSON")],
    title="Dental X-ray Cavity Finder (Mock MVP)",
    description="Prototype — not for clinical use."
)

if __name__ == "__main__":
    demo.launch()
