# This code is just to test if connectivity of all three models (OpenAI, Gemini and Claude) is working fine.


import os
from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI

# Override cached environment variables
load_dotenv(override=True)

#Gemini Base URL to connect to Gemini using OpenAI python library
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

#Reading API Key for Gemini, OpenAI and Claude from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

#Define Models which will be used to for this test
gemini_model = "gemini-2.5-flash"
openai_model = "gpt-4o-mini"
claude_model = "claude-sonnet-4-5-20250929"

#initialize objects for each models
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=GEMINI_API_KEY)
openai = OpenAI(api_key=OPENAI_API_KEY)
claude = Anthropic(api_key=CLAUDE_API_KEY)

#Test message to check the connectivity
messages = [{
    "role": "user",
    "content": "What is the capital of Gujarat, India? Please respond in plain text without any formatting."
}]

#Connect to Gemini
response = gemini.chat.completions.create(
    model=gemini_model,
    messages=messages
)

print("Gemini response: ", response.choices[0].message.content)

#Connect to OpenAI
response = openai.chat.completions.create(
    model=openai_model,
    messages=messages
)

print("OpenAI response: ", response.choices[0].message.content)

#Connect to Claude
response = claude.messages.create(
    model=claude_model,
    messages=messages,
    max_tokens=1024
)

print("Claude response: ", response.content[0].text)
