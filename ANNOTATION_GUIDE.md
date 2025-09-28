
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
