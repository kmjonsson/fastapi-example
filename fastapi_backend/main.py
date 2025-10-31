from .api import app

from .models import init_models

from .api_v1 import init as init_api_v1

init_api_v1(app)

init_models()
