"""
API version 1 initialization for FastAPI application.
"""

from .items import api as items


def init(app):
    app.include_router(items)
