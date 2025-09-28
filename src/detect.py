# src/detect.py
# Detection logic (YOLO wrapper or mock mode)
from PIL import Image
import random
import os

class Detector:
    """YOLO detector with mock fallback for demo purposes."""
    def __init__(self, weights_path="weights/best.pt", mock_ok=True):
        self.weights_path = weights_path
        self.mock_ok = mock_ok
        self.yolo = None
        self.use_mock = True
        
        # Try to load YOLO model
        if not mock_ok:
            try:
                from ultralytics import YOLO
                if os.path.exists(weights_path):
                    self.yolo = YOLO(weights_path)
                    self.use_mock = False
                    print(f"Loaded YOLO model from {weights_path}")
                else:
                    print(f"YOLO weights not found at {weights_path}, using mock mode")
            except ImportError:
                print("ultralytics not available, using mock mode")
            except Exception as e:
                print(f"Error loading YOLO model: {e}, using mock mode")

    def detect(self, img: Image.Image):
        """Detect caries in the image"""
        if self.use_mock or self.yolo is None:
            return self._mock_detect(img)
        else:
            return self._yolo_detect(img)
    
    def _yolo_detect(self, img: Image.Image):
        """Use YOLO model for detection"""
        try:
            results = self.yolo(img)
            detections = []
            
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        conf = float(box.conf[0].cpu().numpy())
                        cls = int(box.cls[0].cpu().numpy())
                        
                        # Map class to caries
                        if conf > 0.5:  # Confidence threshold
                            detections.append({
                                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                                "conf": round(conf, 2),
                                "cls": "caries"
                            })
            
            return detections
            
        except Exception as e:
            print(f"YOLO detection failed: {e}, falling back to mock")
            return self._mock_detect(img)
    
    def _mock_detect(self, img: Image.Image):
        """Mock detection for demo purposes with realistic tooth positions"""
        w, h = img.size
        results = []

        # Generate 0-2 random detections
        num_detections = random.choice([0, 1, 2])

        # Define realistic tooth positions for panoramic X-rays
        tooth_positions = [
            # Upper arch positions (more realistic)
            (0.15, 0.25, 0.20, 0.30),  # Upper right premolar
            (0.25, 0.35, 0.30, 0.40),  # Upper right molar
            (0.35, 0.45, 0.40, 0.50),  # Upper right 2nd molar
            (0.55, 0.65, 0.60, 0.70),  # Upper left premolar
            (0.65, 0.75, 0.70, 0.80),  # Upper left molar
            (0.75, 0.85, 0.80, 0.90),  # Upper left 2nd molar
            
            # Lower arch positions
            (0.20, 0.70, 0.25, 0.75),  # Lower right premolar
            (0.30, 0.60, 0.35, 0.65),  # Lower right molar
            (0.40, 0.50, 0.45, 0.55),  # Lower right 2nd molar
            (0.60, 0.70, 0.65, 0.75),  # Lower left premolar
            (0.70, 0.80, 0.75, 0.85),  # Lower left molar
            (0.80, 0.90, 0.85, 0.95),  # Lower left 2nd molar
        ]

        for _ in range(num_detections):
            # Select a random tooth position
            x_start, y_start, x_end, y_end = random.choice(tooth_positions)
            
            # Convert percentages to pixel coordinates
            x1 = int(w * x_start)
            y1 = int(h * y_start)
            x2 = int(w * x_end)
            y2 = int(h * y_end)
            
            # Add some random variation to make it look more natural
            variation = int(w * 0.02)  # 2% variation
            x1 += random.randint(-variation, variation)
            y1 += random.randint(-variation, variation)
            x2 += random.randint(-variation, variation)
            y2 += random.randint(-variation, variation)
            
            # Ensure box fits in image
            x1 = max(0, min(x1, w - 1))
            y1 = max(0, min(y1, h - 1))
            x2 = max(x1 + 10, min(x2, w - 1))
            y2 = max(y1 + 10, min(y2, h - 1))

            results.append({
                "bbox": [x1, y1, x2, y2],
                "conf": round(random.uniform(0.6, 0.95), 2),
                "cls": "caries"
            })

        return results
