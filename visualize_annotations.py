#!/usr/bin/env python3
"""
Annotation Visualization Tool
Shows bounding boxes on your dental X-rays
"""
import os
from PIL import Image, ImageDraw, ImageFont
import glob

def visualize_annotations():
    """Visualize annotations on images"""
    print("🔍 Visualizing annotations...")
    
    # Get all images
    images = glob.glob('data/images/**/*.jpg', recursive=True) +              glob.glob('data/images/**/*.png', recursive=True)
    
    if not images:
        print("❌ No images found")
        return
    
    for img_path in images:
        # Load image
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        
        # Get corresponding label file
        label_path = img_path.replace('images', 'labels').rsplit('.', 1)[0] + '.txt'
        
        if os.path.exists(label_path):
            # Read annotations
            with open(label_path, 'r') as f:
                lines = f.readlines()
            
            # Draw bounding boxes
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id, center_x, center_y, width, height = map(float, parts)
                    
                    # Convert normalized coordinates to pixel coordinates
                    img_width, img_height = img.size
                    x1 = int((center_x - width/2) * img_width)
                    y1 = int((center_y - height/2) * img_height)
                    x2 = int((center_x + width/2) * img_width)
                    y2 = int((center_y + height/2) * img_height)
                    
                    # Draw rectangle
                    draw.rectangle([x1, y1, x2, y2], outline='red', width=3)
                    
                    # Draw label
                    draw.text((x1, y1-20), f'Caries {class_id}', fill='red')
        
        # Save visualization
        output_path = img_path.replace('images', 'visualizations')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path)
        print(f"   Saved: {output_path}")

if __name__ == "__main__":
    visualize_annotations()
