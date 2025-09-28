# 📧 Temp Mail Setup for Testing

## 🚀 **Quick Temp Mail Setup**

### **Step 1: Get Temp Mail Address**
1. Go to: https://temp-mail.org
2. Copy the temporary email address (e.g., `abc123@temp-mail.org`)
3. Keep the tab open to receive emails

### **Step 2: Create .env File**
Create a `.env` file in your project root with:

```bash
# OpenAI API Key (Required for AI chat)
OPENAI_API_KEY=your-openai-api-key-here

# Temp Mail Configuration (for receiving emails)
EMAIL_USERNAME=your-temp-email@temp-mail.org
EMAIL_PASSWORD=any-password
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
EMAIL_FROM=noreply@dentalclinic.com
```

### **Step 3: Test the Setup**
1. Restart the app:
```bash
python3 flask_app.py
```

2. You should see:
```
✅ Email configuration loaded successfully!
```

## 🎯 **How to Test Email Feature**

### **Option 1: Use Temp Mail for Receiving**
1. **Get temp mail address** from temp-mail.org
2. **Use it in patient form** when testing
3. **Check temp mail inbox** for received emails
4. **See the professional email** with X-ray results

### **Option 2: Use Real Email for Sending**
1. **Use your real email** for sending (Gmail, Outlook, etc.)
2. **Use temp mail address** for receiving
3. **Test the complete workflow**

### **Option 3: Demo Without Email**
1. **Skip email setup** entirely
2. **Use patient portal links** directly
3. **Copy links manually** for testing
4. **Demonstrate all features**

## 📧 **Temp Mail Features**

- **No registration required**
- **Instant email addresses**
- **Receive emails immediately**
- **Perfect for testing**
- **Auto-expires after time**

## 🚀 **Demo Workflow**

1. **Doctor Interface**: `http://127.0.0.1:8080`
   - Upload X-ray and fill patient form
   - Use temp mail address for patient email
   - Get patient portal link

2. **Check Temp Mail**: 
   - Go to temp-mail.org
   - See the professional email
   - Click portal link

3. **Patient Portal**: 
   - Patient accesses personalized results
   - AI chat with personalized responses
   - Insurance pricing and doctor network

## ✅ **Ready to Go**

Your temp mail setup is ready! The app will now send professional emails to the temp mail address with X-ray analysis results.

## 🎯 **Benefits of Temp Mail**

- **No personal email needed**
- **Perfect for testing**
- **Instant setup**
- **Professional demo**
- **No registration required**

## 🚀 **Test Your Setup**

1. **Create `.env` file** with temp mail address
2. **Restart the app**
3. **Upload X-ray** and test email feature
4. **Check temp mail** for received emails

Your dental app is now ready for professional demonstration with temp mail! 🦷📧✨
