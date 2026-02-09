"""
Abstract base class for LLM Providers with concrete implementations.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class LLMProvider(ABC):
    """Abstract base class for all LLM Providers."""

    def __init__(self, api_key: Optional[str]=None) -> None:
        """
        Initialize the LLM Provider

        Args:
            api_key: API key for the provider. If None, will try to load from environment.
        """
        self.api_key = api_key or self._get_api_key()
        self.client = self._initialize_client()
    
    @abstractmethod
    def _get_api_key(self) -> str:
        """ Get API key from environment variables. """
        pass

    @abstractmethod
    def _initialize_client(self) -> Any:
        """Initialize the API client"""
        pass

    @abstractmethod
    def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generate a response from LLM

        Args:
            message: List of message dictionaries with 'role' and 'content' keys.
            **kwargs: Additional parameters specific to the provider
        
        Returns:
            Generated text response.
        """
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Return the model name being used."""
        pass
