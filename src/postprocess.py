# src/postprocess.py
from PIL import ImageDraw, ImageFont
import os

def assign_lesions_to_teeth_and_format(img, detections, tooth_locator):
    """Process detections and create annotated overlay image"""
    base = img.copy().convert("RGB")
    draw = ImageDraw.Draw(base)
    
    # Try to use a better font if available
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()
    
    results = []
    
    for i, det in enumerate(detections):
        x1, y1, x2, y2 = det["bbox"]
        conf = float(det.get("conf", 0.0))
        tooth_id, region = tooth_locator([x1, y1, x2, y2])
        
        # Create result entry
        result = {
            "tooth_id": int(tooth_id), 
            "region": region, 
            "conf": round(conf, 3), 
            "bbox": [int(x1), int(y1), int(x2), int(y2)],
            "cls": det.get("cls", "caries")
        }
        results.append(result)
        
        # Draw bounding box
        draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0), width=3)
        
        # Draw label with background
        label_text = f"#{tooth_id} {region} ({conf:.2f})"
        
        # Get text size for background
        bbox = draw.textbbox((0, 0), label_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Draw background rectangle for text
        text_bg = [x1 + 2, y1 + 2, x1 + 2 + text_width + 4, y1 + 2 + text_height + 4]
        draw.rectangle(text_bg, fill=(255, 255, 255, 180))
        
        # Draw text
        draw.text((x1 + 4, y1 + 4), label_text, fill=(255, 0, 0), font=font)
    
    return results, base
