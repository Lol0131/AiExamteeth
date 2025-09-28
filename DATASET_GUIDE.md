
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
