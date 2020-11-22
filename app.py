import os

from app import create_app

app = create_app(config_name=os.getenv('APP_SETTINGS', 'development'))