# 📧 Simple Email Setup

## 🚀 **Quick Setup Options**

### **Option 1: Use Any Email Provider**
Create a `.env` file in your project root with:

```bash
# OpenAI API Key (Required for AI chat)
OPENAI_API_KEY=your-openai-api-key-here

# Email Configuration (Use any email provider)
EMAIL_USERNAME=your-email@domain.com
EMAIL_PASSWORD=your-email-password
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
EMAIL_FROM=noreply@dentalclinic.com
```

### **Option 2: Use Different Email Providers**

**Gmail:**
```bash
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
```

**Outlook/Hotmail:**
```bash
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
```

**Yahoo:**
```bash
EMAIL_SMTP_SERVER=smtp.mail.yahoo.com
EMAIL_SMTP_PORT=587
```

**Custom Domain:**
```bash
EMAIL_SMTP_SERVER=mail.yourdomain.com
EMAIL_SMTP_PORT=587
```

## 🔧 **For Gmail (Most Common)**

1. **Enable 2-Factor Authentication** in your Google Account
2. **Generate App Password:**
   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this password in `EMAIL_PASSWORD`

3. **Use App Password, NOT your regular password**

## 🎯 **Test Email Setup**

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

## 🚀 **Demo Without Email**

The app works perfectly without email! You can:
- Use patient portal links directly
- Copy links manually
- Test complete workflow
- Demonstrate all features

## ✅ **Ready to Go**

Once you add email credentials to `.env`, the app will automatically:
- Send emails to patients
- Include analysis results
- Provide portal access
- Show email status in doctor interface
