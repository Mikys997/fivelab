from flask import Flask, jsonify
from celery import Celery
import os

app = Flask(__name__)

celery = Celery('service1', broker=os.getenv("CELERY_BROKER_URL"))

@app.route('/send_message', methods=['GET'])
def send_message():
    task = celery.send_task('tasks.process_message', args=["testsdasdasdasdasdasdasddasd"], countdown=10, queue='service2_queue')
    return jsonify({"message": "Message sent to queue with 10-second delay", "task_id": task.id})

@app.route('/')
def service1():
    return "Добро пожаловать в сервис 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
