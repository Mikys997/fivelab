from celery import Celery
import os

celery = Celery('service1', broker=os.getenv("CELERY_BROKER_URL"))

@celery.task(name='tasks.process_message')
def process_message(message):
    print(f"Processed message: {message}")