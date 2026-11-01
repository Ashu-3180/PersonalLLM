"""PersonalLLM package scaffold.

M0 exposes only package metadata and configuration loading.
Tokenizer, model, and training code are intentionally absent.
"""

from personalllm.config import load_config

__all__ = ["__version__", "load_config"]
__version__ = "0.0.1"
