# AI Dental Exam - Complete Doctor & Patient Portal

A comprehensive hackathon prototype featuring AI-powered dental X-ray analysis, patient portals, insurance pricing, and doctor networks with appointment booking.

**Disclaimer**: This is a prototype for educational/demo purposes only — not a medical device and not intended for clinical diagnosis.

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app**:
   ```bash
   python3 flask_app.py
   ```

3. **Open your browser** to: `http://127.0.0.1:8080`

##Complete Features

### Doctor Interface
- **Clean X-ray Analysis**: Upload and analyze X-rays without distracting red boxes
- **Patient Information**: Comprehensive patient data collection (name, age, medical history, insurance)
- **Communication Options**: Email and SMS notifications to patients
- **Patient Portal Links**: Generate shareable links for patient access

### Patient Portal
- **Personalized Welcome**: Customized greeting with visit summary
- **AI Chat Assistant**: Educational AI responses about dental health and findings
- **Insurance Pricing**: Dynamic cost estimates based on actual detection results
- **Doctor Network**: Find alternative providers with competitive pricing
- **Appointment Booking**: Schedule appointments with available doctors

### AI & Detection
- **YOLOv8 Integration**: Real cavity detection with mock fallback
- **Clean Image Display**: Professional X-ray presentation without overlay boxes
- **Confidence Scoring**: High/Medium/Low confidence levels for findings
- **Educational Responses**: Informative AI explanations about dental health

### Insurance & Pricing
- **Dynamic Pricing**: Treatment costs based on actual cavity detection
- **Insurance Integration**: Multiple provider support (Blue Cross, Aetna, Cigna, etc.)
- **Affordable Care**: Competitive pricing for alternative providers
- **Treatment Recommendations**: Filling, crown, root canal, extraction options

## Architecture

### Core Files
- `flask_app.py`: Main Flask application with all routes
- `src/detect.py`: YOLO detection with mock fallback
- `src/tooth_numbering.py`: Tooth ID mapping (Universal/FDI)
- `src/postprocess.py`: Image processing and formatting
- `src/insurance.py`: Mock insurance plans and pricing

### Templates
- `templates/doctor_interface.html`: Doctor's X-ray upload and patient management
- `templates/patient_portal.html`: Patient's personalized results and AI chat

### Configuration
- `.env`: Environment variables for API keys and credentials
- `requirements.txt`: Python dependencies

## Complete Demo Flow

### Doctor Side
1. **Upload X-ray** and enter patient information
2. **Select communication** (email/SMS) options
3. **Analyze X-ray** → Clean image display with text-based findings
4. **Share patient portal link** with patient
5. **Monitor communication status** (sent/not configured)
### Patient Side
1. **Receive personalized welcome** with visit summary
2. **View analysis results** and patient information
3. **Chat with AI** about findings and treatments
4. **Get insurance pricing** based on actual detections
5. **Find alternative doctors** with appointment booking
6. **Schedule appointments** with competitive pricing

## Modern UI Features

- **Maroon & White Theme**: Professional medical aesthetic
- **Floating Effects**: Subtle animations on doctor interface
- **Glass Morphism**: Modern container design with backdrop blur
- **Responsive Design**: Works on desktop and mobile
- **Clean Typography**: Professional medical interface

## Technical Details

- **Flask Web Framework**: Robust Python web application
- **OpenAI Integration**: AI chat with personalized responses
- **Email/SMS Support**: Patient communication (configurable)
- **Mock Data**: Realistic demo data for insurance and doctors
- **Patient Portals**: Unique URLs for each patient's results
- **Appointment System**: Mock booking with available time slots

## Communication Setup

### Email Configuration
```bash
# Add to .env file
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
```

### SMS Configuration (Optional)
```bash
# Add to .env file
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
```

## Hackathon Demo Highlights

This prototype demonstrates:
- **End-to-end workflow**: Doctor analysis → Patient portal → AI chat → Insurance pricing
- **AI-powered analysis**: Real cavity detection with educational explanations
- **Patient engagement**: Personalized portals with AI assistance
- **Healthcare economics**: Insurance integration and competitive pricing
- **Modern UX**: Professional medical interface with smooth animations
- **Scalable architecture**: Flask backend with modular components

## Demo Instructions

1. **Start the app**: `python3 flask_app.py`
2. **Doctor workflow**: Upload X-ray → Enter patient info → Analyze → Share portal link
3. **Patient workflow**: Access portal → Chat with AI → Get pricing → Book appointments
4. **Show features**: Insurance pricing, doctor network, appointment booking

Perfect for healthcare hackathons, AI demos, and medical technology presentations! 🏆
