"""
FastAPI backend package initialization.
"""

from .api import app
from .api_v1 import init as init_api_v1
from .events import init as init_events
from .log import log
from .models import init_models

# Initialize API version 1 and events
init_api_v1(app)
init_events(app)


def initialize_database():
    """Initialize database models."""
    log.info("Initializing database models...")
    init_models()
