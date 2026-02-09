"""
Gemini Provider Implementation
"""

import os
from typing import List, Optional, Dict
from openai import OpenAI
from LLMProvider import LLMProvider

class GeminiProvider(LLMProvider):
    """Gemini provider implementation using OpenAI library"""

    def __init__(self, api_key: Optional[str] = None, model:str = "gemini-2.5-flash") -> None:
        """
        Initialize Gemini Provider

        Args:
            api_key: Gemini API key
            model : Model name to use (default: gemini-2.5-flash).
        """
        self.model = model;
        self.base_uri = "https://generativelanguage.googleapis.com/v1beta/openai/"
        super().__init__(api_key)
    
    def _get_api_key(self) -> str:
        """Get Gemini API key from environment."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        return api_key
    
    def _initialize_client(self) -> OpenAI:
        """Initialize Gemini client using OpenAI library."""
        return OpenAI(base_url=self.base_uri, api_key=self.api_key)
    
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate response using Gemini API

        Args:
            messages: List of messages dictionaries.
            **kwargs: additional parameters.

        Returns:
            Generated text response
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content
    
    def get_model_name(self) -> str:
        """ Return Gemini Model Name """
        return self.model