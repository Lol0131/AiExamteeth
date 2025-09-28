#!/usr/bin/env python3
"""
Quick training script using available datasets
"""
import os
import sys
from ultralytics import YOLO
import torch

def check_dataset(dataset_path):
    """Check if dataset exists and is properly formatted"""
    if not os.path.exists(dataset_path):
        print(f"❌ Dataset not found: {dataset_path}")
        return False
    
    # Check for images
    train_images = os.path.join(dataset_path, "images", "train")
    val_images = os.path.join(dataset_path, "images", "val")
    
    if not os.path.exists(train_images) or not os.path.exists(val_images):
        print(f"❌ Dataset structure incomplete: {dataset_path}")
        return False
    
    # Count images
    train_count = len([f for f in os.listdir(train_images) if f.endswith(('.jpg', '.png', '.jpeg'))])
    val_count = len([f for f in os.listdir(val_images) if f.endswith(('.jpg', '.png', '.jpeg'))])
    
    print(f"📊 Found {train_count} training images, {val_count} validation images")
    
    if train_count == 0:
        print("❌ No training images found")
        return False
    
    return True

def train_with_dataset(dataset_path, epochs=50):
    """Train YOLO model with specified dataset"""
    print(f"🚀 Training with dataset: {dataset_path}")
    
    # Check dataset
    if not check_dataset(dataset_path):
        return False
    
    # Check device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"🖥️  Using device: {device}")
    
    # Load model
    model = YOLO('yolov8n.pt')  # Use nano model for faster training
    
    # Train
    try:
        results = model.train(
            data=f'{dataset_path}/dataset.yaml',
            epochs=epochs,
            imgsz=640,
            batch=8,
            device=device,
            project='runs/train',
            name='caries_detection',
            save=True,
            save_period=10,
            patience=20,
            lr0=0.01,
            weight_decay=0.0005,
            warmup_epochs=3,
            box=7.5,
            cls=0.5,
            dfl=1.5,
            val=True,
            plots=True,
            verbose=True
        )
        
        print("✅ Training completed!")
        print(f"📁 Model saved to: {results.save_dir}")
        print(f"📊 Best model: {results.save_dir}/weights/best.pt")
        
        # Copy to weights directory
        import shutil
        os.makedirs('weights', exist_ok=True)
        shutil.copy(f'{results.save_dir}/weights/best.pt', 'weights/best.pt')
        print("✅ Model copied to weights/best.pt")
        
        return True
        
    except Exception as e:
        print(f"❌ Training failed: {e}")
        return False

def main():
    """Main training function"""
    print("🦷 Quick YOLO Training for Dental Caries Detection")
    print("=" * 60)
    
    # Available datasets
    datasets = {
        'enhanced': 'datasets/enhanced',
        'sample': 'datasets/sample',
        'roboflow': 'datasets/roboflow',
        'tufts': 'datasets/tufts',
        'children': 'datasets/children'
    }
    
    # Check which datasets are available
    available_datasets = []
    for name, path in datasets.items():
        if os.path.exists(path):
            available_datasets.append((name, path))
            print(f"✅ Found dataset: {name} at {path}")
        else:
            print(f"❌ Dataset not found: {name} at {path}")
    
    if not available_datasets:
        print("\n❌ No datasets found!")
        print("📋 Please download datasets first:")
        print("1. Run: python3 download_datasets.py")
        print("2. Download from Roboflow: https://universe.roboflow.com/renielaz/dental-caries-x-ray")
        print("3. Extract to datasets/roboflow/")
        return
    
    # Use the first available dataset
    dataset_name, dataset_path = available_datasets[0]
    print(f"\n🎯 Using dataset: {dataset_name}")
    
    # Train
    success = train_with_dataset(dataset_path, epochs=50)
    
    if success:
        print("\n🎉 Training completed successfully!")
        print("📁 Your trained model is now available at: weights/best.pt")
        print("🌐 Your Flask app will automatically use the trained model!")
    else:
        print("\n❌ Training failed. Please check your dataset and try again.")

if __name__ == "__main__":
    main()
