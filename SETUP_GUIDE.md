# Setup Guide

Complete step-by-step guide to set up the LLM Provider Framework.

## 📋 Prerequisites

Before you begin, ensure you have:

- ✅ Python 3.9 or higher installed
- ✅ pip package manager
- ✅ Git (for cloning the repository)
- ✅ API keys for at least one LLM provider

## 🔧 Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/llm-provider-framework.git
cd llm-provider-framework
```

### Step 2: Create Virtual Environment

#### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `openai` - OpenAI Python SDK
- `anthropic` - Anthropic Claude SDK
- `python-dotenv` - Environment variable management

### Step 4: Set Up Environment Variables

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** and add your API keys:
   ```env
   OPENAI_API_KEY=sk-your-actual-openai-key
   GEMINI_API_KEY=your-actual-gemini-key
   CLAUDE_API_KEY=sk-ant-your-actual-claude-key
   ```

### Step 5: Verify Installation

Run the connection test:

```bash
python ConnectionTestV2.py
```

Expected output:
```
Gemini Response: Gandhinagar
OpenAI Response: Gandhinagar
Claude Response: Gandhinagar
=== Test Complete ====
```

## 🔑 Getting API Keys

### OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (starts with `sk-`)
6. Add to `.env` as `OPENAI_API_KEY`

**Pricing:** Pay-as-you-go, charges based on tokens used

### Google Gemini API Key

1. Go to [Google AI Studio](https://ai.google.dev/)
2. Sign in with Google account
3. Click "Get API key"
4. Create a new API key
5. Copy the key
6. Add to `.env` as `GEMINI_API_KEY`

**Pricing:** Free tier available, then pay-as-you-go

### Anthropic Claude API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to Settings → API Keys
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-`)
6. Add to `.env` as `CLAUDE_API_KEY`

**Pricing:** Pay-as-you-go with free trial credits

## 🧪 Testing Your Setup

### Test 1: Individual Providers

Test each provider separately:

```python
from dotenv import load_dotenv
from ProviderFactory import create_provider

load_dotenv()

# Test OpenAI
try:
    openai = create_provider('openai')
    print("✓ OpenAI connected")
except Exception as e:
    print(f"✗ OpenAI failed: {e}")

# Test Gemini
try:
    gemini = create_provider('gemini')
    print("✓ Gemini connected")
except Exception as e:
    print(f"✗ Gemini failed: {e}")

# Test Claude
try:
    claude = create_provider('claude')
    print("✓ Claude connected")
except Exception as e:
    print(f"✗ Claude failed: {e}")
```

### Test 2: Generate Responses

```python
from ProviderFactory import create_provider

provider = create_provider('claude')
messages = [{"role": "user", "content": "Say hello!"}]
response = provider.generate_response(messages)
print(response)
```

### Test 3: Model Comparison

Run the comparison tool:

```bash
python CompareModels.py
```

## 🐛 Troubleshooting

### Issue: "Module not found"

**Solution:** Make sure virtual environment is activated and dependencies installed:
```bash
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "API key not found"

**Solution:** Check your `.env` file:
- File must be named exactly `.env` (not `.env.txt`)
- File must be in the project root directory
- Keys must be on format: `VARIABLE_NAME=value` (no spaces around `=`)
- Make sure to call `load_dotenv()` in your code

### Issue: "Invalid API key"

**Solution:**
- Verify the key is correct (copy-paste from provider website)
- Check for extra spaces or newlines
- Ensure the key hasn't expired
- Verify your account has credits/billing set up

### Issue: Rate limit errors

**Solution:**
- Add delays between requests
- Reduce request frequency
- Upgrade to paid tier for higher limits

### Issue: Import errors

**Solution:**
```bash
# Make sure you're in the project directory
cd llm-provider-framework

# Verify Python version
python --version  # Should be 3.9+

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## 📚 Next Steps

Once setup is complete:

1. **Read the [README.md](README.md)** for detailed documentation
2. **Try the examples** in the Usage Examples section
3. **Run CompareModels.py** to see providers in action
4. **Build your own application** using the framework

## 💡 Tips

- **Use version control:** Commit your code but never commit `.env`
- **Monitor API usage:** Check your provider dashboards regularly
- **Start with free tiers:** Test with free models before upgrading
- **Handle errors:** Always wrap API calls in try-except blocks
- **Use environment variables:** Never hardcode API keys

## 🆘 Getting Help

If you need help:

1. Check the [README.md](README.md) documentation
2. Search [existing issues](https://github.com/yourusername/llm-provider-framework/issues)
3. Create a new issue with details about your problem
4. Join discussions in the repository

## ✅ Setup Checklist

- [ ] Python 3.9+ installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with API keys
- [ ] Connection test passed
- [ ] Ready to build!

---

**Happy coding! 🚀**
