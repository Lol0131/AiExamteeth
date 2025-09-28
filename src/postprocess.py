# src/postprocess.py
from PIL import ImageDraw

def assign_lesions_to_teeth_and_format(img, detections, tooth_locator):
    base = img.copy().convert("RGB")
    draw = ImageDraw.Draw(base)
    results = []
    for det in detections:
        x1, y1, x2, y2 = det["bbox"]
        conf = float(det.get("conf", 0.0))
        tooth_id, region = tooth_locator([x1, y1, x2, y2])
        results.append({"tooth_id": int(tooth_id), "region": region, "conf": round(conf, 3), "bbox": [int(x1), int(y1), int(x2), int(y2)]})
        draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0), width=3)
        draw.text((x1 + 3, y1 + 3), f"{tooth_id} {region} ({conf:.2f})", fill=(255, 0, 0))
    return results, base
