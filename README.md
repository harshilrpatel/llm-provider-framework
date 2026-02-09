# LLM Provider Framework

A unified Python framework for interacting with multiple Large Language Model (LLM) providers through a single, consistent interface. Built on object-oriented principles with an abstract base class design pattern.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

- **Unified Interface**: Single API to interact with OpenAI, Google Gemini, and Anthropic Claude
- **Abstract Base Class Design**: Clean, extensible architecture following SOLID principles
- **Provider Factory Pattern**: Easy instantiation with automatic provider selection
- **Type-Safe**: Full type hints for better IDE support and code safety
- **Environment-Based Configuration**: Secure API key management using `.env` files
- **Model Comparison Tool**: Built-in utility to compare responses across different LLMs
- **Minimal Dependencies**: Only requires official provider SDKs and python-dotenv

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/harshilrpatel/llm-provider-framework.git
cd llm-provider-framework
```

2. **Create a virtual environment:**
```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**

Create a `.env` file in the project root:

```env
# OpenAI API Key
OPENAI_API_KEY=sk-...

# Google Gemini API Key
GEMINI_API_KEY=your-gemini-api-key

# Anthropic Claude API Key
CLAUDE_API_KEY=sk-ant-...
```

> ⚠️ **Security Note**: Never commit your `.env` file to version control. Add it to `.gitignore`.

## 🎯 Quick Start

### Basic Usage

```python
from dotenv import load_dotenv
from ProviderFactory import create_provider

# Load environment variables
load_dotenv()

# Create a provider
claude = create_provider('claude')

# Generate a response
messages = [{"role": "user", "content": "What is the capital of France?"}]
response = claude.generate_response(messages)
print(response)
```

### Using Different Providers

```python
# OpenAI
openai = create_provider('openai', model='gpt-4o')
response = openai.generate_response(messages)

# Gemini
gemini = create_provider('gemini', model='gemini-2.5-flash')
response = gemini.generate_response(messages)

# Claude
claude = create_provider('claude', model='claude-sonnet-4-5-20250929')
response = claude.generate_response(messages)
```

## 🏗️ Architecture

The framework is built on a clean, object-oriented architecture:

```
┌─────────────────────────┐
│   LLMProvider (ABC)     │  ← Abstract Base Class
├─────────────────────────┤
│ + _get_api_key()        │
│ + _initialize_client()  │
│ + generate_response()   │
│ + get_model_name()      │
└─────────────────────────┘
         ▲    ▲    ▲
         │    │    │
    ┌────┘    │    └────┐
    │         │         │
┌───┴────┐ ┌──┴───┐ ┌───┴──────┐
│OpenAI  │ │Gemini│ │  Claude  │
│Provider│ │Provider│ │Provider │
└────────┘ └──────┘ └──────────┘
```

### Design Principles

- **Single Responsibility**: Each provider manages only its own API integration
- **Open/Closed**: Easy to extend with new providers without modifying existing code
- **Liskov Substitution**: All providers are interchangeable through the base interface
- **Dependency Inversion**: Code depends on abstractions, not concrete implementations

## 📚 Usage Examples

### Example 1: Connection Testing

Test connectivity to all providers:

```bash
python ConnectionTestV2.py
```

### Example 2: Model Comparison

Compare responses from different LLMs on the same question:

```bash
python CompareModels.py
```

This script:
1. Generates a challenging question using a random LLM
2. Asks all three providers to answer the question
3. Uses a random LLM to judge and rank the responses

### Example 3: Custom Implementation

```python
from ProviderFactory import create_provider

# Create provider with custom model
provider = create_provider('openai', model='gpt-4o')

# Multi-turn conversation
conversation = [
    {"role": "user", "content": "Tell me a joke"},
    {"role": "assistant", "content": "Why did the programmer quit? They didn't get arrays!"},
    {"role": "user", "content": "Explain why that's funny"}
]

response = provider.generate_response(conversation)
print(response)
```

### Example 4: Provider-Specific Parameters

```python
# OpenAI with temperature control
openai = create_provider('openai')
response = openai.generate_response(
    messages,
    temperature=0.7,
    max_tokens=500
)

# Claude with extended context
claude = create_provider('claude')
response = claude.generate_response(
    messages,
    max_tokens=2048,
    temperature=0.5
)
```

## 📖 API Reference

### LLMProvider (Abstract Base Class)

Base class that all providers must implement.

#### Methods

- `__init__(api_key: Optional[str] = None)` - Initialize the provider
- `_get_api_key() -> str` - Get API key from environment (abstract)
- `_initialize_client() -> Any` - Initialize the API client (abstract)
- `generate_response(messages: List[Dict[str, str]], **kwargs) -> str` - Generate response (abstract)
- `get_model_name() -> str` - Return the model name (abstract)

### OpenAIProvider

Provider for OpenAI's GPT models.

```python
OpenAIProvider(api_key: Optional[str] = None, model: str = "gpt-4o-mini")
```

**Supported Models:**
- `gpt-4o` - Most capable model
- `gpt-4o-mini` - Faster, cost-effective model
- `gpt-4-turbo` - Previous generation flagship
- `gpt-3.5-turbo` - Fast and efficient

### GeminiProvider

Provider for Google's Gemini models.

```python
GeminiProvider(api_key: Optional[str] = None, model: str = "gemini-2.5-flash")
```

**Supported Models:**
- `gemini-2.5-flash` - Latest fast model
- `gemini-2.0-flash-exp` - Experimental version
- `gemini-pro` - Balanced performance

### ClaudeProvider

Provider for Anthropic's Claude models.

```python
ClaudeProvider(api_key: Optional[str] = None, model: str = "claude-sonnet-4-5-20250929")
```

**Supported Models:**
- `claude-opus-4-5-20251101` - Most capable
- `claude-sonnet-4-5-20250929` - Balanced intelligence and speed
- `claude-haiku-4-5-20251001` - Fast and lightweight

### ProviderFactory

Factory function for creating providers dynamically.

```python
create_provider(provider_name: str, **kwargs) -> LLMProvider
```

**Parameters:**
- `provider_name` - 'openai', 'gemini', or 'claude' (case-insensitive)
- `**kwargs` - Additional parameters passed to provider constructor

**Returns:** LLMProvider instance

**Raises:** ValueError if provider_name is not recognized

## 📁 Project Structure

```
llm-provider-framework/
│
├── LLMProvider.py           # Abstract base class
├── OpenAIProvider.py        # OpenAI implementation
├── GeminiProvider.py        # Gemini implementation
├── ClaudeProvider.py        # Claude implementation
├── ProviderFactory.py       # Factory pattern implementation
│
├── ConnectionTest.py        # Legacy connection test
├── ConnectionTestV2.py      # Modern connection test using factory
├── CompareModels.py         # Model comparison utility
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables

All API keys are loaded from a `.env` file:

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key from platform.openai.com | For OpenAI |
| `GEMINI_API_KEY` | Google AI API key from ai.google.dev | For Gemini |
| `CLAUDE_API_KEY` | Anthropic API key from console.anthropic.com | For Claude |

### Default Models

Each provider has a default model that can be overridden:

- **OpenAI**: `gpt-4o-mini`
- **Gemini**: `gemini-2.5-flash`
- **Claude**: `claude-sonnet-4-5-20250929`

## 🧪 Testing

### Run Connection Tests

Test all provider connections:

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

### Run Model Comparison

Compare LLM responses on a challenging question:

```bash
python CompareModels.py
```

This will:
1. Generate a test question
2. Collect responses from all models
3. Rank them based on quality

## 🛠️ Extending the Framework

### Adding a New Provider

1. Create a new provider class inheriting from `LLMProvider`:

```python
from LLMProvider import LLMProvider
import os

class NewProvider(LLMProvider):
    def __init__(self, api_key=None, model="default-model"):
        self.model = model
        super().__init__(api_key)
    
    def _get_api_key(self) -> str:
        api_key = os.getenv("NEW_PROVIDER_API_KEY")
        if not api_key:
            raise ValueError("NEW_PROVIDER_API_KEY not found")
        return api_key
    
    def _initialize_client(self):
        # Initialize your client here
        return YourClientLibrary(api_key=self.api_key)
    
    def generate_response(self, messages, **kwargs) -> str:
        # Implement response generation
        response = self.client.generate(messages=messages, **kwargs)
        return response.text
    
    def get_model_name(self) -> str:
        return self.model
```

2. Update `ProviderFactory.py`:

```python
from NewProvider import NewProvider

def create_provider(provider_name: str, **kwargs) -> LLMProvider:
    providers = {
        'openai': OpenAIProvider,
        'gemini': GeminiProvider,
        'claude': ClaudeProvider,
        'newprovider': NewProvider  # Add here
    }
    # ... rest of the code
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add some amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Coding Standards

- Follow PEP 8 style guide
- Add type hints to all functions
- Include docstrings for classes and methods
- Write tests for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for GPT models
- [Google](https://ai.google.dev/) for Gemini models
- [Anthropic](https://www.anthropic.com/) for Claude models

## 📞 Support

If you encounter any issues or have questions:

- **Issues**: [GitHub Issues](https://github.com/yourusername/llm-provider-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/llm-provider-framework/discussions)

## 🗺️ Roadmap

- [ ] Add support for Azure OpenAI
- [ ] Implement streaming responses
- [ ] Add async/await support
- [ ] Create comprehensive test suite
- [ ] Add logging and debugging utilities
- [ ] Support for function calling
- [ ] Token usage tracking and cost estimation

## 📊 Requirements

- Python 3.9+
- openai >= 1.85.0
- anthropic >= 0.39.0
- python-dotenv >= 1.1.0
