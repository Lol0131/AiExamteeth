#!/usr/bin/env python3
"""
Data Preparation Script for Dental Caries Detection
Helps you prepare and annotate your dental X-ray dataset
"""
import os
import json
from PIL import Image, ImageDraw, ImageFont
import random

def create_sample_dataset():
    """Create a sample dataset structure with placeholder images"""
    print("📁 Creating sample dataset structure...")
    
    # Create directories
    os.makedirs('data/images/train', exist_ok=True)
    os.makedirs('data/images/val', exist_ok=True)
    os.makedirs('data/labels/train', exist_ok=True)
    os.makedirs('data/labels/val', exist_ok=True)
    os.makedirs('weights', exist_ok=True)
    
    print("✅ Directory structure created")
    
    # Check if we have existing images
    existing_images = []
    for root, dirs, files in os.walk('data/images'):
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg')):
                existing_images.append(os.path.join(root, file))
    
    if existing_images:
        print(f"📊 Found {len(existing_images)} existing images")
        return existing_images
    else:
        print("⚠️  No images found. Please add your dental X-ray images to:")
        print("   - data/images/train/ (for training)")
        print("   - data/images/val/ (for validation)")
        return []

def create_annotation_guide():
    """Create an annotation guide for dental X-rays"""
    guide = """
# 🦷 Dental X-ray Annotation Guide

## YOLO Annotation Format
Each image needs a corresponding .txt file with the same name.

### Format: class_id center_x center_y width height
- All coordinates are normalized (0.0 to 1.0)
- class_id: 0 for caries (cavities)
- center_x, center_y: Center of the bounding box
- width, height: Size of the bounding box

### Example annotation (caries.txt):
```
0 0.5 0.3 0.1 0.15
0 0.7 0.8 0.08 0.12
```

This means:
- 2 caries detected
- First caries: center at (50%, 30%), size 10% x 15%
- Second caries: center at (70%, 80%), size 8% x 12%

## Annotation Tips:
1. **Draw tight boxes** around the caries/cavity
2. **Include the entire lesion** but not too much healthy tooth
3. **Be consistent** with box sizes
4. **Annotate all visible caries** in each image
5. **Use dental numbering** to identify tooth locations

## Tooth Numbering Reference:
- Universal: 1-32 (1-16 upper, 17-32 lower)
- FDI: 11-18, 21-28, 31-38, 41-48

## Quality Guidelines:
- Use high-resolution X-rays (at least 1000px wide)
- Ensure good contrast and visibility
- Include various types of caries (occlusal, interproximal, etc.)
- Balance between healthy and diseased teeth
"""
    
    with open('ANNOTATION_GUIDE.md', 'w') as f:
        f.write(guide)
    
    print("📖 Annotation guide created: ANNOTATION_GUIDE.md")

def create_sample_annotations():
    """Create sample annotation files for existing images"""
    print("📝 Creating sample annotation files...")
    
    # Get all images
    images = []
    for root, dirs, files in os.walk('data/images'):
        for file in files:
            if file.endswith(('.jpg', '.png', '.jpeg')):
                images.append((root, file))
    
    if not images:
        print("⚠️  No images found to annotate")
        return
    
    for root, img_file in images:
        # Create corresponding label file
        label_file = img_file.rsplit('.', 1)[0] + '.txt'
        label_path = os.path.join(root.replace('images', 'labels'), label_file)
        
        if not os.path.exists(label_path):
            # Create sample annotation with random caries
            num_caries = random.randint(0, 3)  # 0-3 caries per image
            
            with open(label_path, 'w') as f:
                for _ in range(num_caries):
                    # Random position and size
                    center_x = random.uniform(0.2, 0.8)
                    center_y = random.uniform(0.2, 0.8)
                    width = random.uniform(0.05, 0.15)
                    height = random.uniform(0.05, 0.15)
                    
                    f.write(f"0 {center_x:.3f} {center_y:.3f} {width:.3f} {height:.3f}\n")
            
            print(f"   Created sample annotation: {label_file} ({num_caries} caries)")
    
    print("✅ Sample annotation files created")
    print("⚠️  IMPORTANT: Replace sample annotations with real bounding box coordinates!")

def create_visualization_tool():
    """Create a tool to visualize annotations"""
    viz_tool = '''#!/usr/bin/env python3
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
    images = glob.glob('data/images/**/*.jpg', recursive=True) + \
             glob.glob('data/images/**/*.png', recursive=True)
    
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
'''
    
    with open('visualize_annotations.py', 'w') as f:
        f.write(viz_tool)
    
    print("🔍 Visualization tool created: visualize_annotations.py")

def create_training_script():
    """Create a simplified training script"""
    training_script = '''#!/usr/bin/env python3
"""
Simplified Training Script
"""
from ultralytics import YOLO
import torch

def train():
    """Train YOLO model"""
    print("🚀 Starting training...")
    
    # Load model
    model = YOLO('yolov8n.pt')
    
    # Train
    results = model.train(
        data='data/dataset.yaml',
        epochs=50,
        imgsz=640,
        batch=8,
        device='cuda' if torch.cuda.is_available() else 'cpu',
        project='runs/train',
        name='caries_detection'
    )
    
    print("✅ Training completed!")
    print(f"📁 Model saved to: {results.save_dir}/weights/best.pt")

if __name__ == "__main__":
    train()
'''
    
    with open('simple_train.py', 'w') as f:
        f.write(training_script)
    
    print("🚀 Simple training script created: simple_train.py")

def main():
    """Main data preparation pipeline"""
    print("🦷 Dental X-ray Data Preparation Pipeline")
    print("=" * 50)
    
    # Step 1: Create dataset structure
    images = create_sample_dataset()
    
    # Step 2: Create annotation guide
    create_annotation_guide()
    
    # Step 3: Create sample annotations
    if images:
        create_sample_annotations()
    
    # Step 4: Create visualization tool
    create_visualization_tool()
    
    # Step 5: Create training script
    create_training_script()
    
    print("\n🎉 Data preparation completed!")
    print("\n📋 Next steps:")
    print("1. Add your dental X-ray images to data/images/train/ and data/images/val/")
    print("2. Annotate them using the guide in ANNOTATION_GUIDE.md")
    print("3. Run: python3 visualize_annotations.py (to check your annotations)")
    print("4. Run: python3 simple_train.py (to train the model)")
    print("5. Copy the trained model to weights/best.pt")

if __name__ == "__main__":
    main()
