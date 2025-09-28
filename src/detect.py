# src/detect.py
# Detection logic (YOLO wrapper or mock mode)
# src/detect.py
from PIL import Image
import random

class Detector:
    """Mock detector: returns 0–2 fake 'caries' boxes so the UI works now."""
    def __init__(self, weights_path="weights/best.pt", mock_ok=True):
        self.weights_path = weights_path
        self.mock_ok = mock_ok
        self.yolo = None  # you can load YOLO later

    def detect(self, img: Image.Image):
        w, h = img.size
        results = []
        for _ in range(random.choice([0, 1, 2])):
            bw, bh = int(w * 0.08), int(h * 0.08)
            x1 = random.randint(int(w * 0.3), int(w * 0.6))
            y1 = random.randint(int(h * 0.3), int(h * 0.6))
            results.append({"bbox": [x1, y1, x1 + bw, y1 + bh], "conf": round(random.uniform(0.6, 0.95), 2), "cls": "caries"})
        return results
