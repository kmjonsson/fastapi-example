from .routers import items
from .models import init_models

def init(app):
    app.include_router(items.api)
    init_models()
