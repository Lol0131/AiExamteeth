# 📧 Hotmail/Outlook Email Setup

## 🚀 **Quick Hotmail Setup**

Create a `.env` file in your project root with these settings:

```bash
# OpenAI API Key (Required for AI chat)
OPENAI_API_KEY=your-openai-api-key-here

# Hotmail/Outlook Email Configuration
EMAIL_USERNAME=your-email@hotmail.com
EMAIL_PASSWORD=your-hotmail-password
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
EMAIL_FROM=noreply@dentalclinic.com
```

## 🔧 **Hotmail/Outlook Settings**

- **SMTP Server**: `smtp-mail.outlook.com`
- **Port**: `587`
- **Security**: TLS/STARTTLS
- **Authentication**: Yes

## 📧 **Supported Email Domains**

- `@hotmail.com`
- `@outlook.com`
- `@live.com`
- `@msn.com`

## 🔐 **Security Requirements**

1. **Use your regular Hotmail password** (no app password needed)
2. **Enable "Less secure app access"** if prompted
3. **Or use 2-factor authentication** with app password

## 🎯 **Test Your Setup**

After creating `.env` file, restart the app:
```bash
python3 flask_app.py
```

You should see:
```
✅ Email configuration loaded successfully!
```

## 📧 **Email Features**

- **Patient Results**: X-ray analysis with overlay image
- **Portal Link**: Direct access to patient portal
- **Professional Format**: Clean, medical-grade emails
- **Attachment Support**: X-ray images included

## 🚀 **Demo Ready**

Once configured, the app will automatically:
- Send emails to patients
- Include analysis results
- Provide portal access
- Show email status in doctor interface

## ✅ **Troubleshooting**

If you get authentication errors:
1. Check your password is correct
2. Try enabling "Less secure app access"
3. Or use 2-factor authentication with app password
4. Make sure you're using the correct SMTP server

## 🎯 **Ready to Go**

Your Hotmail/Outlook email setup is ready! The app will now send professional emails to patients with their X-ray analysis results.
