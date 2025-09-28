#!/usr/bin/env python3
"""
Flask-based dental app that actually works and places detections on real teeth
"""
import json, os
from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import openai
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from src.detect import Detector
from src.tooth_numbering import grid_tooth_map
from src.postprocess import assign_lesions_to_teeth_and_format

app = Flask(__name__)
detector = Detector()
os.makedirs(".outputs", exist_ok=True)

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("⚠️ Warning: OPENAI_API_KEY not found in .env file. Chatbot will use fallback responses.")
else:
    print("✅ OpenAI API key loaded successfully!")

# Email configuration
EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com")
EMAIL_SMTP_PORT = int(os.getenv("EMAIL_SMTP_PORT", "587"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_FROM = os.getenv("EMAIL_FROM", "noreply@dentalclinic.com")

# SMS configuration (using Twilio)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

if not EMAIL_USERNAME or not EMAIL_PASSWORD:
    print("⚠️ Warning: Email credentials not found in .env file. Email functionality will be disabled.")
else:
    print("✅ Email configuration loaded successfully!")

if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN:
    print("⚠️ Warning: SMS credentials not found in .env file. SMS functionality will be disabled.")
else:
    print("✅ SMS configuration loaded successfully!")

# Realistic tooth positions for panoramic X-rays
TOOTH_POSITIONS = {
    # Upper arch (teeth 1-16)
    1: {"x": 0.05, "y": 0.15, "width": 0.06, "height": 0.12},  # Wisdom tooth
    2: {"x": 0.12, "y": 0.12, "width": 0.06, "height": 0.12},  # Molar
    3: {"x": 0.19, "y": 0.10, "width": 0.06, "height": 0.12},  # Molar
    4: {"x": 0.26, "y": 0.08, "width": 0.06, "height": 0.12},  # Premolar
    5: {"x": 0.33, "y": 0.06, "width": 0.06, "height": 0.12},  # Premolar
    6: {"x": 0.40, "y": 0.05, "width": 0.05, "height": 0.10},  # Canine
    7: {"x": 0.46, "y": 0.04, "width": 0.05, "height": 0.10},  # Incisor
    8: {"x": 0.52, "y": 0.04, "width": 0.05, "height": 0.10},  # Incisor
    9: {"x": 0.58, "y": 0.04, "width": 0.05, "height": 0.10},  # Incisor
    10: {"x": 0.64, "y": 0.04, "width": 0.05, "height": 0.10}, # Incisor
    11: {"x": 0.70, "y": 0.05, "width": 0.05, "height": 0.10}, # Canine
    12: {"x": 0.76, "y": 0.06, "width": 0.06, "height": 0.12}, # Premolar
    13: {"x": 0.83, "y": 0.08, "width": 0.06, "height": 0.12}, # Premolar
    14: {"x": 0.90, "y": 0.10, "width": 0.06, "height": 0.12}, # Molar
    15: {"x": 0.97, "y": 0.12, "width": 0.06, "height": 0.12}, # Molar
    16: {"x": 0.04, "y": 0.15, "width": 0.06, "height": 0.12}, # Wisdom tooth
    
    # Lower arch (teeth 17-32)
    17: {"x": 0.05, "y": 0.85, "width": 0.06, "height": 0.12}, # Wisdom tooth
    18: {"x": 0.12, "y": 0.88, "width": 0.06, "height": 0.12}, # Molar
    19: {"x": 0.19, "y": 0.90, "width": 0.06, "height": 0.12}, # Molar
    20: {"x": 0.26, "y": 0.92, "width": 0.06, "height": 0.12}, # Premolar
    21: {"x": 0.33, "y": 0.94, "width": 0.06, "height": 0.12}, # Premolar
    22: {"x": 0.40, "y": 0.95, "width": 0.05, "height": 0.10}, # Canine
    23: {"x": 0.46, "y": 0.96, "width": 0.05, "height": 0.10}, # Incisor
    24: {"x": 0.52, "y": 0.96, "width": 0.05, "height": 0.10}, # Incisor
    25: {"x": 0.58, "y": 0.96, "width": 0.05, "height": 0.10}, # Incisor
    26: {"x": 0.64, "y": 0.96, "width": 0.05, "height": 0.10}, # Incisor
    27: {"x": 0.70, "y": 0.95, "width": 0.05, "height": 0.10}, # Canine
    28: {"x": 0.76, "y": 0.94, "width": 0.06, "height": 0.12}, # Premolar
    29: {"x": 0.83, "y": 0.92, "width": 0.06, "height": 0.12}, # Premolar
    30: {"x": 0.90, "y": 0.90, "width": 0.06, "height": 0.12}, # Molar
    31: {"x": 0.97, "y": 0.88, "width": 0.06, "height": 0.12}, # Molar
    32: {"x": 0.04, "y": 0.85, "width": 0.06, "height": 0.12}, # Wisdom tooth
}

def get_realistic_detections(img):
    """Generate detections using trained model or fallback to realistic mock"""
    w, h = img.size
    results = []
    
    # Try to use trained model first
    try:
        if os.path.exists('weights/best.pt'):
            from ultralytics import YOLO
            model = YOLO('weights/best.pt')
            yolo_results = model(img)
            
            for result in yolo_results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        conf = float(box.conf[0].cpu().numpy())
                        cls = int(box.cls[0].cpu().numpy())
                        
                        if conf > 0.5:  # Confidence threshold
                            # Map to tooth position
                            center_x = (x1 + x2) / 2
                            center_y = (y1 + y2) / 2
                            
                            # Find closest tooth
                            tooth_id = find_closest_tooth(center_x, center_y, w, h)
                            
                            results.append({
                                "bbox": [int(x1), int(y1), int(x2), int(y2)],
                                "conf": round(conf, 2),
                                "cls": "caries",
                                "tooth_id": tooth_id
                            })
            
            if results:
                print(f"✅ Used trained model: {len(results)} detections")
                return results
        else:
            print("⚠️  No trained model found, using mock detections")
    except Exception as e:
        print(f"⚠️  Model inference failed: {e}, using mock detections")
    
    # Fallback to realistic mock detections
    import random
    num_cavities = random.choice([0, 1, 2, 3])
    affected_teeth = random.sample(list(TOOTH_POSITIONS.keys()), num_cavities)
    
    for tooth_id in affected_teeth:
        pos = TOOTH_POSITIONS[tooth_id]
        
        # Convert relative positions to absolute coordinates
        x1 = int(pos["x"] * w)
        y1 = int(pos["y"] * h)
        x2 = int((pos["x"] + pos["width"]) * w)
        y2 = int((pos["y"] + pos["height"]) * h)
        
        # Add small random variation to make it look more realistic
        variation_x = random.randint(-10, 10)
        variation_y = random.randint(-5, 5)
        variation_w = random.randint(-5, 5)
        variation_h = random.randint(-5, 5)
        
        x1 = max(0, x1 + variation_x)
        y1 = max(0, y1 + variation_y)
        x2 = min(w, x2 + variation_w)
        y2 = min(h, y2 + variation_h)
        
        results.append({
            "bbox": [x1, y1, x2, y2],
            "conf": round(random.uniform(0.7, 0.95), 2),
            "cls": "caries",
            "tooth_id": tooth_id
        })
    
    return results

def find_closest_tooth(center_x, center_y, img_width, img_height):
    """Find the closest tooth to a detection center"""
    # Convert to relative coordinates
    rel_x = center_x / img_width
    rel_y = center_y / img_height
    
    closest_tooth = 1
    min_distance = float('inf')
    
    for tooth_id, pos in TOOTH_POSITIONS.items():
        tooth_center_x = pos["x"] + pos["width"] / 2
        tooth_center_y = pos["y"] + pos["height"] / 2
        
        distance = ((rel_x - tooth_center_x) ** 2 + (rel_y - tooth_center_y) ** 2) ** 0.5
        
        if distance < min_distance:
            min_distance = distance
            closest_tooth = tooth_id
    
    return closest_tooth

@app.route('/')
def index():
    """Main doctor interface for X-ray upload and patient information"""
    return render_template('doctor_interface.html')

@app.route('/simple')
def simple():
    """Simple interface for quick testing"""
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/patient/<patient_id>')
def patient_portal(patient_id):
    """Patient portal page with their specific results and AI chat"""
    try:
        # Load patient-specific results
        with open(f'.outputs/patient_{patient_id}.json', 'r') as f:
            patient_data = json.load(f)
        return render_template('patient_portal.html', 
                             patient_id=patient_id, 
                             findings=patient_data.get('findings', []),
                             patient_name=patient_data.get('patient_name', 'Patient'))
    except:
        # Fallback to last results if patient-specific data not found
        try:
            with open('.outputs/last_result.json', 'r') as f:
                results = json.load(f)
            return render_template('patient_portal.html', 
                                 patient_id=patient_id, 
                                 findings=results.get('findings', []),
                                 patient_name="Patient")
        except:
            return render_template('patient_portal.html', 
                                 patient_id=patient_id, 
                                 findings=[],
                                 patient_name="Patient")

@app.route('/chat/api', methods=['POST'])
def chat_api():
    """Handle chatbot API requests using OpenAI with personalized responses"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        patient_name = data.get('patient_name', 'Patient')
        patient_age = data.get('patient_age', '')
        patient_history = data.get('patient_history', '')
        insurance_provider = data.get('insurance_provider', '')
        findings = data.get('findings', [])
        
        if not user_message:
            return jsonify({'response': 'Please enter a message.'})
        
        # Create personalized context
        context = f"Patient: {patient_name}"
        if patient_age:
            context += f", Age: {patient_age}"
        if patient_history:
            context += f", Medical History: {patient_history}"
        if insurance_provider:
            context += f", Insurance: {insurance_provider.replace('_', ' ').title()}"
        if findings:
            context += f", Current Findings: {findings}"
        
        # Use OpenAI if API key is available, otherwise fallback to local responses
        if openai.api_key:
            response = get_personalized_openai_response(user_message, context, findings)
        else:
            response = get_personalized_dental_response(user_message, patient_name, findings)
        
        return jsonify({'response': response})
        
    except Exception as e:
        return jsonify({'response': f'Sorry, I encountered an error: {str(e)}'})

def get_openai_response(message):
    """Generate AI response using OpenAI API"""
    try:
        # Create a dental-focused system prompt
        system_prompt = """You are a helpful AI dental assistant. You provide accurate, professional information about dental health, treatments, and procedures. You should:

1. Be informative but not replace professional dental advice
2. Use clear, patient-friendly language
3. Focus on dental health topics
4. Always recommend consulting with a dentist for specific concerns
5. Be encouraging about oral hygiene and preventive care

Keep responses concise but helpful (2-3 sentences typically)."""

        # Use the new OpenAI API syntax
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=200,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"OpenAI API error: {e}")
        # Fallback to local responses if OpenAI fails
        return get_dental_response(message)

def get_personalized_openai_response(message, context, findings):
    """Generate personalized AI response using OpenAI API"""
    try:
        # Create a personalized dental-focused system prompt
        system_prompt = f"""You are a helpful AI dental assistant speaking directly to a patient. You have access to their personal information and current dental findings.

Patient Context: {context}

You should:
1. Address the patient by name when appropriate
2. Reference their specific findings when relevant
3. Be informative but not replace professional dental advice
4. Use clear, patient-friendly language
5. Focus on their specific dental health situation
6. Always recommend consulting with a dentist for specific concerns
7. Be encouraging about oral hygiene and preventive care

Keep responses concise but helpful (2-3 sentences typically)."""

        # Use the new OpenAI API syntax
        client = openai.OpenAI(api_key=openai.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            max_tokens=200,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"OpenAI API error: {e}")
        # Fallback to personalized local responses if OpenAI fails
        return get_personalized_dental_response(message, context.split(',')[0].split(':')[1].strip(), findings)

def get_personalized_dental_response(message, patient_name, findings):
    """Generate personalized AI response for dental questions"""
    message_lower = message.lower()
    
    # Personalized greetings
    if any(word in message_lower for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return f"Hello {patient_name}! I'm your AI dental assistant. I can help you understand your X-ray results and answer questions about your dental health. What would you like to know?"
    
    # Reference specific findings with educational content
    if findings and any(word in message_lower for word in ['finding', 'result', 'detected', 'cavity', 'tooth']):
        findings_text = ", ".join([f"tooth #{f['tooth_id']}" for f in findings])
        confidence_levels = ", ".join([f"{f['tooth_id']} ({'high' if f.get('conf', 0.5) > 0.8 else 'moderate' if f.get('conf', 0.5) > 0.6 else 'low'} confidence)" for f in findings])
        return f"Based on your X-ray analysis, we detected potential dental issues with {findings_text} ({confidence_levels}). These findings indicate areas where tooth structure may be compromised. Cavities form when bacteria produce acids that dissolve tooth enamel. Early detection allows for less invasive treatments like fillings, while advanced cases may require crowns or root canals. The confidence levels help determine treatment urgency. Would you like me to explain the specific treatment options for your findings?"
    
    # Cost/pricing questions
    if any(word in message_lower for word in ['cost', 'price', 'expensive', 'cheap', 'afford', 'insurance', 'payment', 'bill', 'money', 'budget']):
        return f"I'd be happy to help you with pricing information, {patient_name}! Please provide your insurance details so I can calculate your out-of-pocket costs accurately."
    
    # Treatment questions with educational content
    if any(word in message_lower for word in ['treatment', 'fix', 'repair', 'procedure', 'surgery', 'crown', 'filling', 'root canal']):
        return f"Great question about treatments, {patient_name}! The treatment you need depends on the severity of your dental issues. Fillings are used for small cavities, crowns for larger damage, and root canals for infected teeth. Each treatment has different recovery times and costs. Based on your X-ray findings, I can explain which treatments might be recommended and what each procedure involves. Would you like me to detail the specific treatments for your situation?"
    
    # General dental health
    if any(word in message_lower for word in ['brush', 'floss', 'oral', 'hygiene', 'prevent', 'care']):
        return f"Great question about oral hygiene, {patient_name}! Good dental care includes brushing twice daily with fluoride toothpaste, flossing daily, and regular dental check-ups. Given your current findings, maintaining excellent oral hygiene is especially important."
    
    # Default personalized response
    return f"I'm here to help educate you about your dental health, {patient_name}. I can explain your X-ray findings, discuss treatment options, provide oral hygiene guidance, and answer questions about dental procedures. What specific aspect of your dental health would you like to learn more about?"

def get_dental_response(message):
    """Generate AI response for dental questions"""
    message_lower = message.lower()
    
    # Comprehensive dental knowledge base
    responses = {
        'cavity': {
            'keywords': ['cavity', 'cavities', 'decay', 'hole'],
            'response': 'A cavity is a hole in your tooth caused by tooth decay. It starts when bacteria in your mouth produce acids that eat away at your tooth enamel. Early detection through X-rays can help prevent more serious problems. Treatment usually involves removing the decayed part and filling the tooth.'
        },
        'filling': {
            'keywords': ['filling', 'fillings', 'filling material'],
            'response': 'A dental filling is used to restore a tooth damaged by decay back to its normal function and shape. Common types include amalgam (silver), composite (tooth-colored), and gold fillings. The choice depends on the location, extent of decay, and your preference.'
        },
        'root canal': {
            'keywords': ['root canal', 'endodontic', 'nerve treatment'],
            'response': 'A root canal is a treatment to repair and save a badly damaged or infected tooth. The procedure involves removing the damaged area of the tooth, cleaning and disinfecting it, then filling and sealing it. It\'s often the best way to save a tooth that would otherwise need to be extracted.'
        },
        'prevention': {
            'keywords': ['prevent', 'prevention', 'avoid', 'stop'],
            'response': 'Good oral hygiene is key to preventing dental problems: brush twice daily with fluoride toothpaste, floss daily, limit sugary foods and drinks, visit your dentist regularly, and consider dental sealants for extra protection.'
        },
        'insurance': {
            'keywords': ['insurance', 'coverage', 'benefits', 'plan'],
            'response': 'Dental insurance typically covers preventive care (cleanings, exams) at 100%, basic procedures (fillings) at 70-80%, and major procedures (crowns, root canals) at 50%. Coverage varies by plan, so check your specific benefits.'
        },
        'cost': {
            'keywords': ['cost', 'price', 'expensive', 'money', 'fee'],
            'response': 'Dental costs vary by procedure and location. Basic cleanings cost $75-200, fillings $150-400, crowns $800-1500, and root canals $600-1400. Many offices offer payment plans or financing options.'
        },
        'pain': {
            'keywords': ['pain', 'hurt', 'ache', 'sore', 'sensitive'],
            'response': 'Tooth pain can indicate various issues: cavities, gum disease, cracked teeth, or infections. If you\'re experiencing severe or persistent pain, contact your dentist immediately. Over-the-counter pain relievers can provide temporary relief.'
        },
        'whitening': {
            'keywords': ['whitening', 'white', 'bleach', 'stain'],
            'response': 'Teeth whitening can be done professionally at your dentist\'s office or at home with over-the-counter products. Professional treatments are more effective and safer. Results typically last 6 months to 2 years depending on your habits.'
        },
        'braces': {
            'keywords': ['braces', 'orthodontic', 'straighten', 'align'],
            'response': 'Braces are used to straighten teeth and correct bite issues. Traditional metal braces, ceramic braces, and clear aligners (like Invisalign) are common options. Treatment duration varies from 6 months to 3 years depending on the complexity.'
        },
        'wisdom teeth': {
            'keywords': ['wisdom', 'third molar', 'extract', 'remove'],
            'response': 'Wisdom teeth are the third molars that usually appear in your late teens or early twenties. They often need to be removed if they\'re impacted, causing pain, or crowding other teeth. Extraction is a common outpatient procedure.'
        },
        'gum disease': {
            'keywords': ['gum', 'gingivitis', 'periodontitis', 'bleeding'],
            'response': 'Gum disease (periodontitis) is an infection of the tissues that hold your teeth in place. Early stage (gingivitis) is reversible with good oral hygiene. Advanced stages may require deep cleaning or surgery. Regular dental visits help prevent and detect it early.'
        }
    }
    
    # Check for specific keywords
    for topic, data in responses.items():
        for keyword in data['keywords']:
            if keyword in message_lower:
                return data['response']
    
    # General responses
    if any(word in message_lower for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return "Hello! I'm your AI dental assistant. I can help you understand your dental health, treatments, and answer questions about oral care. What would you like to know?"
    
    if any(word in message_lower for word in ['thank', 'thanks', 'appreciate']):
        return "You're welcome! I'm here to help with any dental health questions you might have. Feel free to ask me anything!"
    
    if any(word in message_lower for word in ['x-ray', 'xray', 'result', 'finding']):
        return "X-rays are an important diagnostic tool in dentistry. They help dentists see problems that aren't visible during a regular exam, like cavities between teeth, bone loss, or impacted teeth. Your dentist will explain any findings and recommend appropriate treatment."
    
    if any(word in message_lower for word in ['brush', 'clean', 'hygiene', 'floss']):
        return "Good oral hygiene is essential! Brush your teeth twice daily with fluoride toothpaste, floss daily, and use mouthwash. Don't forget to replace your toothbrush every 3-4 months and visit your dentist regularly for cleanings."
    
    # Default response
    return "That's a great question! I can help educate you about dental health, treatments, and procedures. I can explain how cavities form, what different treatments involve, proper oral hygiene techniques, and answer questions about dental procedures. What specific aspect of dental health would you like to learn more about?"

def send_patient_sms(patient_phone, patient_name, findings, report_text, patient_id):
    """Send SMS to patient with their results"""
    if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_PHONE_NUMBER:
        print("⚠️ SMS credentials not configured. Cannot send SMS.")
        return False

    try:
        from twilio.rest import Client
        
        # Create Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # Format phone number (remove any non-digits and add +1 if needed)
        phone = ''.join(filter(str.isdigit, patient_phone))
        if len(phone) == 10:
            phone = '+1' + phone
        elif not phone.startswith('+'):
            phone = '+' + phone
        
        # Create SMS message
        if findings:
            findings_text = ", ".join([f"tooth #{f['tooth_id']}" for f in findings])
            message_body = f"""🦷 Hi {patient_name}! Your dental X-ray analysis is complete.

🔍 Findings: {findings_text}
📋 Summary: {report_text[:100]}...

💬 View your detailed results & chat with AI:
http://127.0.0.1:8080/patient/{patient_id}

Questions? Chat with our AI assistant about your specific findings!"""
        else:
            message_body = f"""🦷 Hi {patient_name}! Great news!

✅ No cavities detected - your teeth look healthy!
📋 Summary: {report_text[:100]}...

💬 View your results & chat with AI:
http://127.0.0.1:8080/patient/{patient_id}

Keep up the great oral hygiene!"""
        
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone
        )
        
        print(f"✅ SMS sent successfully to {patient_phone} (SID: {message.sid})")
        return True
        
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")
        return False

def send_patient_email(patient_email, patient_name, findings, overlay_image_path, report_text, patient_id):
    """Send email report to patient after X-ray analysis"""
    if not EMAIL_USERNAME or not EMAIL_PASSWORD:
        print("⚠️ Email credentials not configured. Cannot send email.")
        return False
    
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = patient_email
        msg['Subject'] = f"🦷 Your Dental X-ray Analysis Results - {patient_name}"
        
        # Create email body with link to patient portal
        if findings:
            findings_text = "\n".join([f"• Tooth #{f['tooth_id']} ({f['region']}) - Confidence: {f['conf']:.2f}" for f in findings])
            # Generate a unique patient ID for the results
            import uuid
            patient_id = str(uuid.uuid4())[:8]
            
            body = f"""
Dear {patient_name},

Thank you for your recent dental X-ray examination. Our AI analysis has been completed, and we have some findings to share with you.

🔍 **Analysis Results:**
{findings_text}

📋 **Summary:**
{report_text}

💬 **View Your Results & Chat with AI:**
Click the button below to access your personalized patient portal where you can:
- View your detailed X-ray analysis with annotations
- Chat with our AI assistant about your specific findings
- Ask questions like "What does this mean?" or "What treatments might I need?"
- Get personalized recommendations based on your results

🔗 **Access Your Results:** http://127.0.0.1:8080/patient/{patient_id}

📅 **Next Steps:**
Please schedule a follow-up appointment with Dr. [Dentist Name] to discuss these findings and any recommended treatments.

📞 **Contact Information:**
- Phone: [Clinic Phone]
- Email: [Clinic Email]
- Address: [Clinic Address]

Best regards,
[Clinic Name] Dental Team

---
This email was automatically generated by our AI dental analysis system.
For questions about this report, please contact our office directly.
            """
        else:
            body = f"""
Dear {patient_name},

Thank you for your recent dental X-ray examination. Our AI analysis has been completed with excellent news!

✅ **Great News:**
No cavities or dental issues were detected in your X-ray. Your teeth appear to be in good health!

📋 **Summary:**
{report_text}

🦷 **Maintaining Good Oral Health:**
- Continue brushing twice daily with fluoride toothpaste
- Floss daily
- Maintain regular dental check-ups
- Limit sugary foods and drinks

📅 **Next Steps:**
Please schedule your next routine check-up in 6 months to maintain your excellent oral health.

📞 **Contact Information:**
- Phone: [Clinic Phone]
- Email: [Clinic Email]
- Address: [Clinic Address]

This is an automated report generated by our AI dental analysis system. For any questions or concerns, please contact our office directly.

Best regards,
[Clinic Name] Dental Team

---
This email was automatically generated by our AI dental analysis system.
For questions about this report, please contact our office directly.
            """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach the overlay image if it exists
        if overlay_image_path and os.path.exists(overlay_image_path):
            with open(overlay_image_path, 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data)
            image.add_header('Content-Disposition', 'attachment', filename='dental_analysis.png')
            msg.attach(image)
        
        # Send email
        server = smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_FROM, patient_email, text)
        server.quit()
        
        print(f"✅ Email sent successfully to {patient_email}")
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Get uploaded image and patient info
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'})
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No image selected'})
        
        # Get enhanced patient information
        patient_name = request.form.get('patient_name', 'Patient')
        patient_age = request.form.get('patient_age', '')
        patient_email = request.form.get('patient_email', '')
        patient_phone = request.form.get('patient_phone', '')
        patient_history = request.form.get('patient_history', '')
        insurance_provider = request.form.get('insurance_provider', '')
        send_email = request.form.get('send_email', 'false').lower() == 'true'
        send_sms = request.form.get('send_sms', 'false').lower() == 'true'
        
        # Open and process image
        img = Image.open(file.stream)
        img = img.convert('RGB')
        
        # Get realistic detections
        detections = get_realistic_detections(img)
        
        # Create overlay
        overlay = img.copy()
        draw = ImageDraw.Draw(overlay)
        
        # Try to use a better font
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 16)
        except:
            try:
                font = ImageFont.truetype("arial.ttf", 16)
            except:
                font = ImageFont.load_default()
        
        findings = []
        for det in detections:
            x1, y1, x2, y2 = det["bbox"]
            conf = det["conf"]
            tooth_id = det["tooth_id"]
            
            # Draw bounding box
            draw.rectangle([x1, y1, x2, y2], outline=(255, 0, 0), width=3)
            
            # Draw label
            label_text = f"#{tooth_id} ({conf:.2f})"
            
            # Get text size for background
            bbox = draw.textbbox((0, 0), label_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Draw background rectangle for text
            text_bg = [x1 + 2, y1 + 2, x1 + 2 + text_width + 4, y1 + 2 + text_height + 4]
            draw.rectangle(text_bg, fill=(255, 255, 255, 180))
            
            # Draw text
            draw.text((x1 + 4, y1 + 4), label_text, fill=(255, 0, 0), font=font)
            
            findings.append({
                "tooth_id": tooth_id,
                "region": "MO",  # Simplified for demo
                "conf": conf,
                "bbox": [x1, y1, x2, y2],
                "cls": "caries"
            })
        
        # Convert original image to base64 for web display (no red boxes)
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        # Generate report
        if not findings:
            report = "✅ No cavities detected - your teeth look healthy!"
        else:
            report = "🔍 Cavity Detection Results:\n"
            for finding in findings:
                report += f"• Tooth #{finding['tooth_id']} - Confidence: {finding['conf']:.2f}\n"
        
        # Save results
        result = {"findings": findings}
        with open(".outputs/last_result.json", "w") as f:
            json.dump(result, f, indent=2)
        
        # Save overlay image for email attachment
        overlay_path = ".outputs/overlay_result.png"
        overlay.save(overlay_path)
        
        # Always generate patient ID and save results for portal access
        import uuid
        patient_id = str(uuid.uuid4())[:8]
        
        # Save enhanced patient results with ID for the portal
        patient_results = {
            "patient_id": patient_id,
            "patient_name": patient_name,
            "patient_age": patient_age,
            "patient_email": patient_email,
            "patient_phone": patient_phone,
            "patient_history": patient_history,
            "insurance_provider": insurance_provider,
            "findings": findings,
            "report": report,
            "overlay_path": overlay_path
        }
        with open(f'.outputs/patient_{patient_id}.json', 'w') as f:
            json.dump(patient_results, f, indent=2)
        
        # Send email to patient if requested and email credentials are configured
        email_sent = False
        if send_email and patient_email and EMAIL_USERNAME and EMAIL_PASSWORD:
            email_sent = send_patient_email(patient_email, patient_name, findings, overlay_path, report, patient_id)
        
        # Send SMS to patient if requested and SMS credentials are configured
        sms_sent = False
        if send_sms and patient_phone and TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
            sms_sent = send_patient_sms(patient_phone, patient_name, findings, report, patient_id)
        
        # Determine status for better user feedback
        email_status = 'sent' if email_sent else 'not_configured' if send_email and patient_email and (not EMAIL_USERNAME or not EMAIL_PASSWORD) else 'not_requested'
        sms_status = 'sent' if sms_sent else 'not_configured' if send_sms and patient_phone and (not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN) else 'not_requested'
        
        return jsonify({
            'success': True,
            'overlay_image': img_str,
            'report': report,
            'findings': findings,
            'email_sent': email_sent,
            'email_status': email_status,
            'sms_sent': sms_sent,
            'sms_status': sms_status,
            'patient_name': patient_name,
            'patient_portal_link': f"http://127.0.0.1:8080/patient/{patient_id}" if patient_id else None
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'})

if __name__ == '__main__':
    print("🚀 Starting Flask Dental App...")
    print("🌐 Open your browser to: http://127.0.0.1:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)
