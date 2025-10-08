from django.core.management import call_command
from django.db.utils import OperationalError
import time

def run():
    from django.conf import settings
    if settings.DEBUG is False:  # Only on Render
        try:
            call_command('loaddata', 'pizzas.json')
            print("✅ Pizzas loaded successfully!")
        except OperationalError:
            print("⚠️ Database not ready, retrying...")
            time.sleep(5)
            run()