"""
Connection test using the abstract LLM provider classes
"""

from dotenv import load_dotenv
from ProviderFactory import create_provider

#Load environment variables
load_dotenv(override=True)

#Test Message
messages = [{
    "role" : "user",
    "content": "What is the capital of Gujarat, India?"
}]

print(f"messages: {messages}")

def main():
    """Main Function to test all providers"""
    print("String LLM Provider Connection Tests...")

    gemini = create_provider('Gemini')
    openai = create_provider('OpenAI')
    claude = create_provider('Claude')

    print(f"Gemini Response: {gemini.generate_response(messages)}")
    print(f"OpenAI Response: {openai.generate_response(messages)}")
    print(f"Claude Response: {claude.generate_response(messages)}")

    print("=== Test Complete ====")

if __name__== "__main__":
    main()
