# 🤖 AI Dental Chatbot Setup

Your Flask app now includes an AI-powered dental chatbot! Here's how to set it up:

## 🚀 Quick Start

1. **Set your OpenAI API key** (if you have one):
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

2. **Start the Flask app**:
   ```bash
   python3 flask_app.py
   ```

3. **Open your browser** to:
   - Main app: http://127.0.0.1:8080
   - Chat page: http://127.0.0.1:8080/chat

## 🔑 OpenAI API Key Setup

### Option 1: .env File (Recommended)
Create a `.env` file in your project root:
```bash
# .env file
OPENAI_API_KEY=your-openai-api-key-here
```

### Option 2: Environment Variable
```bash
# macOS/Linux
export OPENAI_API_KEY='your-api-key-here'

# Windows (Command Prompt)
set OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY='your-api-key-here'
```

### Option 3: Get API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy and add it to your `.env` file

## 💬 Chatbot Features

The AI chatbot can help with:
- **Dental Health Questions**: Cavities, gum disease, oral hygiene
- **Treatment Information**: Fillings, root canals, braces, whitening
- **Cost & Insurance**: Pricing estimates, coverage questions
- **Prevention Tips**: Brushing, flossing, diet advice
- **X-ray Results**: Understanding findings and next steps

## 🔄 Fallback Mode

If no OpenAI API key is set, the chatbot will use built-in dental knowledge responses. This ensures the app works even without API access.

## 🎯 Example Questions to Try

- "What is a cavity?"
- "How much does a filling cost?"
- "What should I do about tooth pain?"
- "Tell me about dental insurance"
- "How can I prevent gum disease?"
- "What are the benefits of braces?"

## 🛠️ Technical Details

- **AI Model**: GPT-3.5-turbo (when API key is available)
- **Fallback**: Local dental knowledge base
- **Response Time**: ~1-2 seconds
- **Max Tokens**: 200 (concise responses)
- **Temperature**: 0.7 (balanced creativity/accuracy)

## 🚨 Important Notes

- The chatbot provides general information only
- Always consult a dentist for specific concerns
- Not a replacement for professional dental advice
- Responses are educational and supportive

Enjoy your AI dental assistant! 🦷✨
