"""
Claude (Anthropic) provider implementation
"""

import os
from typing import List, Dict, Optional
from anthropic import Anthropic
from LLMProvider import LLMProvider

class ClaudeProvider(LLMProvider):
    """ Claude (Anthropic) provider implementation """

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-sonnet-4-5-20250929") -> None:
        """
        Initialize Claude provider

        Args:
            api_key: Claude API key
            model: Model Name to use (default: claude-sonnet-4-5-20250929).
        """
        self.model = model
        super().__init__(api_key)
    
    def _get_api_key(self) -> str:
        """Get Claude API key from environment"""
        api_key = os.getenv("CLAUDE_API_KEY")
        if not api_key:
            raise ValueError("CLAUDE_API_KEY not found in environment variables")
        return api_key
    
    def _initialize_client(self) -> Anthropic:
        """Initialize Anthropic client."""
        return Anthropic(api_key=self.api_key)
    
    def generate_response(self, messages: List[Dict[str, str]], max_tokens:int = 1024, **kwargs) -> str:
        """
        Generate response using Claude API.

        Args:
            messages: List of message dictionaries.
            max_tokens: Maximum tokens in response (required in Claude).
            ***kwarg: Additional Claude parameters.

        Returns:
            Generated text response.
        """
        response = self.client.messages.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens,
            **kwargs
        )
        return response.content[0].text
    
    def get_model_name(self) -> str:
        """Return the Claude model name"""
        return self.model
