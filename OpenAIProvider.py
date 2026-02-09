"""
Open AI provider implementation
"""

import os
from pyexpat import model
from typing import List, Dict, Optional
from openai import OpenAI
from LLMProvider import LLMProvider

class OpenAIProvider(LLMProvider):
    """ OpenAI provider implementation """
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o-mini") -> None:
        """
        Initialize OpenAI provider

        Args:
            api_key: OpenAI API key
            model: Model name to use (default: gpt-40-mini)
        """
        self.model = model
        super().__init__(api_key)
    
    def _get_api_key(self) -> str:
        """ Get OpenAI API key from environment """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in evironment variables")
        return api_key
    
    def _initialize_client(self) -> OpenAI:
        return OpenAI(api_key=self.api_key)

    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate response using OpenAI API.

        Args:
            messages: List of message dictionaries.
            ***kwargs: Additional OpenAI parameters (temperaturem max_tokens, etc.)
        
        Returns:
            Generated text response
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages = messages,
            **kwargs
        )
        return response.choices[0].message.content

    def get_model_name(self) -> str:
        """ Return the OpenAI model name"""
        return self.model
