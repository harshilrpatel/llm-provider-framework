"""
Factory function to create LLM providers
"""

from LLMProvider import LLMProvider
from OpenAIProvider import OpenAIProvider
from GeminiProvider import GeminiProvider
from ClaudeProvider import ClaudeProvider

def create_provider(provider_name: str, **kwargs) -> LLMProvider:
    """
    Factory function to create LLM Provider.

    Args: 
        provider_name: Name of the provider ('openai', 'gemini', or 'claude')
        **kwargs: Additional args to pass to the provider constructor.

    Returns:
        LLMProvider instance
    
    Raises:
        ValueError: if provider_name is not reconized.

    Examples:
        >>> provider = create_provider('openai', model='gpt-4o')
        >>> provider = create_provider('claude', model='claude-sonnet-4-5-20250929')
        >>> provider = create_provider('gemini', model='gemini-2.0-flash-exp')
    """
    providers = {
        'openai': OpenAIProvider,
        'gemini': GeminiProvider,
        'claude': ClaudeProvider
    }

    provider_class = providers.get(provider_name.lower())
    if not provider_name:
        raise ValueError(
            f"Unknown Provider: {provider_name}. "
            f"Choose from: {list(providers.keys())}"
        )
    
    return provider_class(**kwargs)