#!/usr/bin/env python3
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
