from .items import router as items


def init(app):
    app.include_router(items.api)
