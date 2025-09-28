# 🦷 AI Training Guide for Dental Caries Detection

## 🚀 Quick Start

### 1. Prepare Your Data
```bash
# Run the data preparation script
python3 prepare_data.py
```

### 2. Add Your Dental X-rays
- Place your dental X-ray images in:
  - `data/images/train/` (for training)
  - `data/images/val/` (for validation)

### 3. Annotate Your Images
- For each image, create a corresponding `.txt` file in:
  - `data/labels/train/` (for training)
  - `data/labels/val/` (for validation)

**Annotation Format:**
```
class_id center_x center_y width height
```
- All coordinates are normalized (0.0 to 1.0)
- `class_id`: 0 for caries
- Example: `0 0.5 0.3 0.1 0.15` (caries at center 50%, 30% with size 10% x 15%)

### 4. Visualize Your Annotations
```bash
# Check if your annotations are correct
python3 visualize_annotations.py
```

### 5. Train the Model
```bash
# Start training
python3 simple_train.py
```

### 6. Use the Trained Model
- The trained model will be saved to `runs/train/caries_detection/weights/best.pt`
- Copy it to `weights/best.pt` to use in your Flask app:
```bash
cp runs/train/caries_detection/weights/best.pt weights/best.pt
```

## 📊 Dataset Requirements

### Minimum Dataset Size:
- **Training**: 50+ images
- **Validation**: 10+ images
- **Total**: 60+ annotated dental X-rays

### Image Quality:
- **Resolution**: At least 1000px wide
- **Format**: JPG, PNG, or JPEG
- **Contrast**: Good visibility of teeth and caries
- **Variety**: Different types of caries (occlusal, interproximal, etc.)

### Annotation Quality:
- **Accuracy**: Tight bounding boxes around caries
- **Consistency**: Same annotation style across all images
- **Completeness**: All visible caries annotated
- **Quality**: Clear, unambiguous lesions

## 🎯 Training Tips

### 1. Data Augmentation
The training script includes:
- Random rotation
- Random brightness/contrast
- Random scaling
- Random flipping

### 2. Training Parameters
- **Epochs**: 50 (adjust based on your dataset size)
- **Batch Size**: 8 (reduce if you get memory errors)
- **Image Size**: 640x640 pixels
- **Learning Rate**: 0.01 (automatically adjusted)

### 3. Monitoring Training
- Check `runs/train/caries_detection/` for:
  - Training plots
  - Validation results
  - Model checkpoints

### 4. Early Stopping
- Training stops if no improvement for 20 epochs
- Best model is automatically saved

## 🔧 Troubleshooting

### Common Issues:

#### 1. "No images found"
- Make sure images are in `data/images/train/` and `data/images/val/`
- Check file extensions (.jpg, .png, .jpeg)

#### 2. "CUDA out of memory"
- Reduce batch size in `simple_train.py`
- Use smaller image size (e.g., 416 instead of 640)

#### 3. "Poor detection accuracy"
- Add more training data
- Improve annotation quality
- Increase training epochs
- Check for class imbalance

#### 4. "Model not loading"
- Make sure `weights/best.pt` exists
- Check file permissions
- Verify model was trained successfully

## 📈 Expected Results

### Good Training Indicators:
- **Loss decreasing**: Training and validation loss should decrease
- **mAP increasing**: Mean Average Precision should improve
- **Precision/Recall**: Both should be > 0.7 for good performance

### Performance Targets:
- **mAP@0.5**: > 0.7 (70% accuracy)
- **Precision**: > 0.8 (80% of detections are correct)
- **Recall**: > 0.7 (70% of caries are detected)

## 🚀 Advanced Training

### Custom Training Parameters:
```python
# In simple_train.py, modify:
results = model.train(
    data='data/dataset.yaml',
    epochs=100,        # More epochs
    imgsz=640,        # Image size
    batch=16,         # Batch size
    lr0=0.01,         # Learning rate
    weight_decay=0.0005,  # Weight decay
    warmup_epochs=3,  # Warmup epochs
    patience=20,      # Early stopping
    save_period=10,   # Save every 10 epochs
)
```

### Model Selection:
- **YOLOv8n**: Fastest, smallest (good for demos)
- **YOLOv8s**: Balanced speed/accuracy
- **YOLOv8m**: Better accuracy, slower
- **YOLOv8l**: Best accuracy, slowest

## 📝 Annotation Tools

### Recommended Tools:
1. **LabelImg**: Free, easy to use
2. **Roboflow**: Online annotation tool
3. **CVAT**: Advanced annotation platform
4. **Label Studio**: Open source annotation

### Annotation Workflow:
1. Load image in annotation tool
2. Draw bounding box around caries
3. Assign class label (caries)
4. Export in YOLO format
5. Save as `.txt` file

## 🎉 Success Checklist

- [ ] 60+ annotated dental X-rays
- [ ] Images in correct directories
- [ ] Annotations in YOLO format
- [ ] Training runs without errors
- [ ] Model achieves >70% mAP
- [ ] Trained model copied to `weights/best.pt`
- [ ] Flask app uses trained model

## 📞 Support

If you encounter issues:
1. Check the error messages
2. Verify your data format
3. Ensure sufficient training data
4. Try different training parameters
5. Check GPU memory usage

Happy training! 🦷✨
