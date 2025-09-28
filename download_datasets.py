#!/usr/bin/env python3
"""
Download and prepare dental datasets for training
"""
import os
import requests
import zipfile
import shutil
from pathlib import Path

def download_roboflow_dataset():
    """Download the Roboflow dental caries dataset"""
    print("🔍 Downloading Roboflow Dental Caries Dataset...")
    
    # Roboflow dataset URL (you'll need to get the actual download link)
    dataset_url = "https://universe.roboflow.com/renielaz/dental-caries-x-ray"
    
    print("📋 To download the Roboflow dataset:")
    print("1. Go to: https://universe.roboflow.com/renielaz/dental-caries-x-ray")
    print("2. Click 'Download Dataset'")
    print("3. Choose 'YOLO v8' format")
    print("4. Download the ZIP file")
    print("5. Extract it to 'datasets/roboflow/'")
    
    return False

def download_sample_dataset():
    """Create a sample dataset structure for testing"""
    print("📁 Creating sample dataset structure...")
    
    # Create directories
    os.makedirs('datasets/sample/images/train', exist_ok=True)
    os.makedirs('datasets/sample/images/val', exist_ok=True)
    os.makedirs('datasets/sample/labels/train', exist_ok=True)
    os.makedirs('datasets/sample/labels/val', exist_ok=True)
    
    # Copy existing images to sample dataset
    if os.path.exists('data/images/train'):
        for img in os.listdir('data/images/train'):
            if img.endswith(('.jpg', '.png', '.jpeg')):
                shutil.copy(f'data/images/train/{img}', f'datasets/sample/images/train/{img}')
                print(f"   Copied: {img}")
    
    if os.path.exists('data/images/val'):
        for img in os.listdir('data/images/val'):
            if img.endswith(('.jpg', '.png', '.jpeg')):
                shutil.copy(f'data/images/val/{img}', f'datasets/sample/images/val/{img}')
                print(f"   Copied: {img}")
    
    print("✅ Sample dataset created in datasets/sample/")
    return True

def create_dataset_config():
    """Create dataset configuration files"""
    print("📝 Creating dataset configuration...")
    
    # Sample dataset config
    sample_config = {
        'path': './datasets/sample',
        'train': 'images/train',
        'val': 'images/val',
        'nc': 1,
        'names': ['caries']
    }
    
    with open('datasets/sample/dataset.yaml', 'w') as f:
        import yaml
        yaml.dump(sample_config, f, default_flow_style=False)
    
    print("✅ Dataset configuration created")
    return True

def download_tufts_dataset():
    """Download Tufts Dental Database"""
    print("🔍 Tufts Dental Database Information:")
    print("📋 To access Tufts dataset:")
    print("1. Go to: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11412602/")
    print("2. Follow the data access instructions")
    print("3. Request access to the dataset")
    print("4. Download and extract to 'datasets/tufts/'")
    
    return False

def download_children_dataset():
    """Download Children's Dental Panoramic Radiographs Dataset"""
    print("🔍 Children's Dental Dataset Information:")
    print("📋 To access Children's dataset:")
    print("1. Go to: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10267170/")
    print("2. Follow the data access instructions")
    print("3. Download the dataset")
    print("4. Extract to 'datasets/children/'")
    
    return False

def create_annotation_guide():
    """Create annotation guide for datasets"""
    guide = """
# 🦷 Dataset Annotation Guide

## Available Datasets:

### 1. Roboflow Dental Caries Dataset
- **URL**: https://universe.roboflow.com/renielaz/dental-caries-x-ray
- **Format**: YOLO v8
- **Features**: Pre-annotated, ready to use
- **Size**: Medium dataset

### 2. Tufts Dental Database
- **URL**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11412602/
- **Format**: Various formats available
- **Features**: Multimodal panoramic X-rays
- **Size**: Large dataset

### 3. Children's Dental Dataset
- **URL**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10267170/
- **Format**: Segmentation masks
- **Features**: 100 panoramic radiographs
- **Size**: Small but high-quality dataset

## Quick Start with Roboflow:

1. **Download Dataset**:
   ```bash
   # Go to Roboflow website and download YOLO v8 format
   # Extract to datasets/roboflow/
   ```

2. **Use Sample Dataset**:
   ```bash
   python3 download_datasets.py --use-sample
   ```

3. **Train Model**:
   ```bash
   python3 simple_train.py --data datasets/sample/dataset.yaml
   ```

## Dataset Structure:
```
datasets/
├── sample/
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   └── dataset.yaml
├── roboflow/
│   ├── images/
│   ├── labels/
│   └── dataset.yaml
└── tufts/
    ├── images/
    ├── labels/
    └── dataset.yaml
```
"""
    
    with open('DATASET_GUIDE.md', 'w') as f:
        f.write(guide)
    
    print("📖 Dataset guide created: DATASET_GUIDE.md")

def main():
    """Main dataset download pipeline"""
    print("🦷 Dental Dataset Downloader")
    print("=" * 40)
    
    # Create dataset directories
    os.makedirs('datasets', exist_ok=True)
    
    # Create sample dataset
    print("\n1. Creating sample dataset...")
    download_sample_dataset()
    
    # Create dataset config
    print("\n2. Creating dataset configuration...")
    create_dataset_config()
    
    # Create annotation guide
    print("\n3. Creating dataset guide...")
    create_annotation_guide()
    
    # Show available datasets
    print("\n4. Available datasets:")
    download_roboflow_dataset()
    download_tufts_dataset()
    download_children_dataset()
    
    print("\n🎉 Dataset setup completed!")
    print("\n📋 Next steps:")
    print("1. Download datasets from the URLs above")
    print("2. Extract them to the datasets/ directory")
    print("3. Run: python3 simple_train.py --data datasets/sample/dataset.yaml")
    print("4. Or use your own dataset by following the guide")

if __name__ == "__main__":
    main()
