from .api import app

from .models import init_models

from .api_v1 import init as init_api_v1
from .events import init as init_events

init_api_v1(app)
init_events(app)

init_models()
