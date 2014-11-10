"""
Loads the application settings.

TODO: Add in development settings, fix production settings
"""

from shesays_platform.settings.base import *

try:
    # Load local_settings, only exist in production
    from local_settings import *
except ImportError:
    # Assume that we're in a development environment
    # TODO: make sure this can be overrided for sqlite dev
    from dev import *
