from fastapi_backend.database import Base, engine

def init_models(engine=engine):
    Base.metadata.create_all(bind=engine)
