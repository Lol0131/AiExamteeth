# 🔧 Email Authentication Fix

## ❌ Current Issue:
```
Error sending email: (535, b'5.7.3 Authentication unsuccessful')
```

## ✅ Quick Fix Options:

### Option 1: Disable Email (Recommended for Demo)
Add this to your `.env` file:
```
EMAIL_USERNAME=
EMAIL_PASSWORD=
```

### Option 2: Fix Gmail Authentication
1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
3. **Update `.env` file**:
   ```
   EMAIL_USERNAME=your_email@gmail.com
   EMAIL_PASSWORD=your_16_character_app_password
   EMAIL_SMTP_SERVER=smtp.gmail.com
   EMAIL_SMTP_PORT=587
   ```

### Option 3: Use Different Email Provider
**Outlook/Hotmail:**
```
EMAIL_USERNAME=your_email@outlook.com
EMAIL_PASSWORD=your_password
EMAIL_SMTP_SERVER=smtp-mail.outlook.com
EMAIL_SMTP_PORT=587
```

**Yahoo:**
```
EMAIL_USERNAME=your_email@yahoo.com
EMAIL_PASSWORD=your_app_password
EMAIL_SMTP_SERVER=smtp.mail.yahoo.com
EMAIL_SMTP_PORT=587
```

## 🚀 Test Your Fix:
1. Update your `.env` file with correct credentials
2. Restart the app: `python3 flask_app.py`
3. Test email sending in the app

## 💡 Demo Tip:
For demo purposes, you can just disable email by leaving EMAIL_USERNAME and EMAIL_PASSWORD empty in your `.env` file. The app will still work and show the patient portal link.
