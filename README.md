# 🦷 AI Dental Exam - Cavity Detection & Insurance

A hackathon prototype that uses AI to analyze dental X-ray images, detect cavities, and provide insurance cost estimates.

⚠️ **Disclaimer**: This is a prototype for educational/demo purposes only — not a medical device and not intended for clinical diagnosis.

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   python app.py
   ```

3. **Open your browser** to the URL shown in the terminal (usually `http://127.0.0.1:7860`)

## ✨ Features

- **AI Detection**: Uses YOLOv8 with mock fallback to detect cavities
- **Tooth Numbering**: Maps detections to tooth IDs using Universal (1-32) or FDI notation
- **Visual Overlay**: Draws red bounding boxes with tooth numbers and confidence scores
- **Insurance Pricing**: Mock insurance plans with cost estimates
- **Patient Assistant**: Friendly messages explaining findings to patients
- **JSON Output**: Structured data for integration with other systems

## 🏗️ Architecture

- `src/detect.py`: YOLO detection with mock fallback
- `src/tooth_numbering.py`: Tooth ID mapping (Universal/FDI)
- `src/postprocess.py`: Image overlay and formatting
- `src/insurance.py`: Mock insurance plans and pricing
- `app.py`: Gradio web interface

## 📊 Demo Flow

1. Upload an X-ray image
2. Select tooth notation system (Universal/FDI)
3. Choose insurance plan
4. Click "Analyze X-ray"
5. View results:
   - Annotated image with red boxes
   - Dentist report
   - JSON detections
   - Patient message
   - Insurance pricing

## 🔧 Technical Details

- **Mock Mode**: Works without YOLO weights for demo purposes
- **Tooth Mapping**: 2x16 grid system for 32 teeth
- **Surface Detection**: MO/DO/BO/LO region mapping
- **Insurance Plans**: 5 mock plans with different coverage rates
- **CDT Codes**: Standard dental procedure codes for billing

## 📝 Example Output

```json
{
  "findings": [
    {
      "tooth_id": 30,
      "region": "MO", 
      "conf": 0.82,
      "bbox": [100, 200, 150, 250],
      "cls": "caries"
    }
  ]
}
```

## 🎯 Hackathon Demo

This prototype demonstrates:
- AI-powered medical image analysis
- Integration with insurance systems
- Patient-friendly interfaces
- Clinical workflow automation
