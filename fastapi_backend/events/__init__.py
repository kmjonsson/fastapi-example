from .github import router as github


def init(app):
    app.include_router(github.api)
