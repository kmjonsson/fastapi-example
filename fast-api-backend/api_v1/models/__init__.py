from database import Base, engine

def init_models():
    Base.metadata.create_all(bind=engine)