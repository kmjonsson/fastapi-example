from .github import api as github


def init(app):
    app.include_router(github)
