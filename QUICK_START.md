
# 🦷 Quick Start Guide - Getting Real Dental Data

## 🚀 **Option 1: Use Enhanced Sample Dataset (Immediate)**
```bash
# Train with enhanced sample dataset
python3 quick_train.py --data datasets/enhanced/dataset.yaml
```

## 🌟 **Option 2: Download Real Datasets (Recommended)**

### **A. Roboflow Dataset (Easiest)**
1. Go to: https://universe.roboflow.com/renielaz/dental-caries-x-ray
2. Click "Download Dataset"
3. Choose "YOLO v8" format
4. Download ZIP file
5. Extract to `datasets/roboflow/`
6. Train: `python3 quick_train.py --data datasets/roboflow/dataset.yaml`

### **B. Children's Dental Dataset**
1. Go to: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10267170/
2. Follow data access instructions
3. Download and extract to `datasets/children/`
4. Convert to YOLO format if needed

### **C. Annotated Intraoral Dataset (6,313 images)**
1. Go to: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12297690/
2. Follow data access instructions
3. Download and extract to `datasets/intraoral/`
4. Convert to YOLO format if needed

## 🔧 **Training Commands**
```bash
# Train with any dataset
python3 quick_train.py --data datasets/[dataset_name]/dataset.yaml

# Train with more epochs for better results
python3 quick_train.py --data datasets/roboflow/dataset.yaml --epochs 100
```

## 📊 **Expected Results**
- **With real data**: 80-95% accuracy
- **With sample data**: 60-70% accuracy
- **Training time**: 10-30 minutes depending on dataset size

## 🎯 **Next Steps**
1. Download a real dataset
2. Train the model
3. Test with your Flask app
4. Iterate and improve!
