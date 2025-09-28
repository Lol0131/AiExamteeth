#!/usr/bin/env python3
"""
YOLO Training Script for Dental Caries Detection
"""
import os
import yaml
from ultralytics import YOLO
import torch

def create_dataset_config():
    """Create dataset configuration for YOLO training"""
    dataset_config = {
        'path': './data',  # Dataset root dir
        'train': 'images/train',  # Train images (relative to 'path')
        'val': 'images/val',  # Val images (relative to 'path')
        'test': 'images/test',  # Test images (relative to 'path')
        
        # Classes
        'nc': 1,  # Number of classes
        'names': ['caries']  # Class names
    }
    
    # Save dataset config
    with open('data/dataset.yaml', 'w') as f:
        yaml.dump(dataset_config, f, default_flow_style=False)
    
    print("✅ Dataset configuration created: data/dataset.yaml")
    return dataset_config

def prepare_training_data():
    """Prepare training data structure"""
    print("🔧 Preparing training data structure...")
    
    # Create directories
    os.makedirs('data/images/train', exist_ok=True)
    os.makedirs('data/images/val', exist_ok=True)
    os.makedirs('data/images/test', exist_ok=True)
    os.makedirs('data/labels/train', exist_ok=True)
    os.makedirs('data/labels/val', exist_ok=True)
    os.makedirs('data/labels/test', exist_ok=True)
    
    print("✅ Directory structure created")
    
    # Check if we have existing data
    train_images = len([f for f in os.listdir('data/images/train') if f.endswith(('.jpg', '.png', '.jpeg'))])
    val_images = len([f for f in os.listdir('data/images/val') if f.endswith(('.jpg', '.png', '.jpeg'))])
    
    print(f"📊 Found {train_images} training images")
    print(f"📊 Found {val_images} validation images")
    
    if train_images == 0:
        print("⚠️  No training images found. Please add dental X-ray images to data/images/train/")
        print("   Each image should have a corresponding .txt file in data/labels/train/")
        print("   Format: class_id center_x center_y width height (normalized 0-1)")
        return False
    
    return True

def create_sample_annotations():
    """Create sample annotation files for existing images"""
    print("📝 Creating sample annotation files...")
    
    # Get existing images
    train_images = [f for f in os.listdir('data/images/train') if f.endswith(('.jpg', '.png', '.jpeg'))]
    
    for img_file in train_images:
        # Create corresponding label file
        label_file = img_file.rsplit('.', 1)[0] + '.txt'
        label_path = f'data/labels/train/{label_file}'
        
        if not os.path.exists(label_path):
            # Create sample annotation (you'll need to replace with real annotations)
            with open(label_path, 'w') as f:
                # Sample annotation: class_id center_x center_y width height
                # This is a placeholder - replace with real bounding box coordinates
                f.write("0 0.5 0.5 0.1 0.1\n")  # class 0 (caries), center at (0.5, 0.5), size 0.1x0.1
            
            print(f"   Created sample annotation: {label_file}")
    
    print("✅ Sample annotation files created")
    print("⚠️  IMPORTANT: Replace sample annotations with real bounding box coordinates!")

def train_model():
    """Train YOLO model for caries detection"""
    print("🚀 Starting YOLO training...")
    
    # Check if CUDA is available
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"🖥️  Using device: {device}")
    
    # Load YOLO model (YOLOv8n for faster training, YOLOv8s for better accuracy)
    model = YOLO('yolov8n.pt')  # You can use 'yolov8s.pt' for better accuracy
    
    # Train the model
    results = model.train(
        data='data/dataset.yaml',
        epochs=100,  # Number of training epochs
        imgsz=640,   # Image size
        batch=16,    # Batch size (reduce if you get memory errors)
        device=device,
        project='runs/train',
        name='caries_detection',
        save=True,
        save_period=10,  # Save checkpoint every 10 epochs
        patience=20,     # Early stopping patience
        lr0=0.01,       # Initial learning rate
        lrf=0.01,       # Final learning rate
        momentum=0.937, # SGD momentum
        weight_decay=0.0005,  # Optimizer weight decay
        warmup_epochs=3,      # Warmup epochs
        warmup_momentum=0.8,   # Warmup momentum
        warmup_bias_lr=0.1,   # Warmup bias learning rate
        box=7.5,        # Box loss gain
        cls=0.5,        # Class loss gain
        dfl=1.5,        # DFL loss gain
        pose=12.0,      # Pose loss gain
        kobj=2.0,       # Keypoint object loss gain
        label_smoothing=0.0,  # Label smoothing
        nbs=64,         # Nominal batch size
        overlap_mask=True,    # Overlap mask
        mask_ratio=4,   # Mask ratio
        dropout=0.0,    # Dropout
        val=True,       # Validate during training
        plots=True,     # Generate training plots
        verbose=True,   # Verbose output
        seed=0,         # Random seed
        deterministic=True,  # Deterministic training
        single_cls=False,    # Single class training
        rect=False,     # Rectangular training
        cos_lr=False,   # Cosine LR scheduler
        close_mosaic=10,     # Close mosaic augmentation
        resume=False,   # Resume training
        amp=True,       # Automatic Mixed Precision
        fraction=1.0,   # Dataset fraction
        profile=False,  # Profile ONNX and TensorRT speeds
        freeze=None,    # Freeze layers
        multi_scale=False,   # Multi-scale training
        overlap_mask=True,   # Overlap mask
        mask_ratio=4,        # Mask ratio
        dropout=0.0,         # Dropout
        val=True,            # Validate during training
        plots=True,          # Generate training plots
        verbose=True,        # Verbose output
        seed=0,              # Random seed
        deterministic=True,  # Deterministic training
        single_cls=False,    # Single class training
        rect=False,          # Rectangular training
        cos_lr=False,        # Cosine LR scheduler
        close_mosaic=10,    # Close mosaic augmentation
        resume=False,        # Resume training
        amp=True,            # Automatic Mixed Precision
        fraction=1.0,        # Dataset fraction
        profile=False,       # Profile ONNX and TensorRT speeds
        freeze=None,         # Freeze layers
        multi_scale=False,   # Multi-scale training
    )
    
    print("✅ Training completed!")
    print(f"📁 Model saved to: {results.save_dir}")
    print(f"📊 Best model: {results.save_dir}/weights/best.pt")
    
    return results

def validate_model(model_path):
    """Validate the trained model"""
    print("🔍 Validating trained model...")
    
    # Load the trained model
    model = YOLO(model_path)
    
    # Validate on validation set
    results = model.val(
        data='data/dataset.yaml',
        imgsz=640,
        batch=16,
        device='cuda' if torch.cuda.is_available() else 'cpu',
        project='runs/val',
        name='caries_validation',
        save=True,
        save_txt=True,
        save_conf=True,
        save_json=True,
        plots=True,
        verbose=True
    )
    
    print("✅ Validation completed!")
    print(f"📊 Validation results: {results}")
    
    return results

def main():
    """Main training pipeline"""
    print("🦷 YOLO Training Pipeline for Dental Caries Detection")
    print("=" * 60)
    
    # Step 1: Create dataset configuration
    create_dataset_config()
    
    # Step 2: Prepare training data
    if not prepare_training_data():
        print("❌ No training data found. Please add images and annotations first.")
        return
    
    # Step 3: Create sample annotations (if needed)
    create_sample_annotations()
    
    # Step 4: Train the model
    print("\n🚀 Starting training...")
    results = train_model()
    
    # Step 5: Validate the model
    print("\n🔍 Validating model...")
    model_path = f"{results.save_dir}/weights/best.pt"
    validate_model(model_path)
    
    print("\n🎉 Training pipeline completed!")
    print(f"📁 Best model: {model_path}")
    print("💡 Copy this model to 'weights/best.pt' to use in your Flask app")

if __name__ == "__main__":
    main()