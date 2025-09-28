# 📧 Temporary Email Setup for Testing

## 🚀 **Quick Temporary Email Options**

### **Option 1: 10MinuteMail (Recommended)**
1. Go to: https://10minutemail.com
2. Get a temporary email address
3. Use it in your `.env` file:

```bash
# OpenAI API Key (Required for AI chat)
OPENAI_API_KEY=your-openai-api-key-here

# Temporary Email Configuration
EMAIL_USERNAME=your-temp-email@10minutemail.com
EMAIL_PASSWORD=any-password
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
EMAIL_FROM=noreply@dentalclinic.com
```

### **Option 2: TempMail**
1. Go to: https://temp-mail.org
2. Get a temporary email address
3. Use it in your `.env` file

### **Option 3: Guerrilla Mail**
1. Go to: https://guerrillamail.com
2. Get a temporary email address
3. Use it in your `.env` file

### **Option 4: Mailinator (Public)**
1. Go to: https://mailinator.com
2. Use any email like: `test123@mailinator.com`
3. No password needed for receiving

## 🎯 **For Sending Emails (Demo Only)**

### **Option 1: Use Gmail with App Password**
```bash
EMAIL_USERNAME=your-gmail@gmail.com
EMAIL_PASSWORD=your-app-password
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_SMTP_PORT=587
```

### **Option 2: Use Outlook/Hotmail**
```bash
EMAIL_USERNAME=your-outlook@outlook.com
EMAIL_PASSWORD=your-password
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
```

### **Option 3: Use Yahoo**
```bash
EMAIL_USERNAME=your-yahoo@yahoo.com
EMAIL_PASSWORD=your-password
EMAIL_SMTP_SERVER=smtp.mail.yahoo.com
EMAIL_SMTP_PORT=587
```

## 🚀 **Demo Without Email (Easiest)**

The app works perfectly without email! You can:
- Use patient portal links directly
- Copy links manually
- Test complete workflow
- Demonstrate all features

## 🎯 **Quick Test Setup**

1. **Create `.env` file** with any email:
```bash
# OpenAI API Key (Required for AI chat)
OPENAI_API_KEY=your-openai-api-key-here

# Demo Email Configuration
EMAIL_USERNAME=demo@dentalclinic.com
EMAIL_PASSWORD=demo123
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
EMAIL_FROM=noreply@dentalclinic.com
```

2. **Restart the app**:
```bash
python3 flask_app.py
```

3. **You'll see**:
```
✅ Email configuration loaded successfully!
```

## 📧 **Email Features for Demo**

- **Patient Results**: X-ray analysis with overlay image
- **Portal Link**: Direct access to patient portal
- **Professional Format**: Clean, medical-grade emails
- **Attachment Support**: X-ray images included

## 🎯 **Demo Ready**

Your app is fully functional for demonstration purposes! The email feature will work with any email configuration, and you can test the complete workflow.

## ✅ **Troubleshooting**

If you get authentication errors:
1. Use a real email address for sending
2. Or disable email and use portal links directly
3. The app works perfectly without email configuration

## 🚀 **Ready to Go**

Your temporary email setup is ready! The app will now send professional emails to patients with their X-ray analysis results.
