import os
from django.apps import AppConfig
from dotenv import load_dotenv

load_dotenv()

class ListenerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = os.getenv('APP_NAME')
