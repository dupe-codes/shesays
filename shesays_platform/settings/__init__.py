"""
Loads the application settings.

TODO: Add in development settings, fix production settings
"""

from shesays_platform.settings.base import *

try:
    from local_settings import *
except ImportError:
    pass
