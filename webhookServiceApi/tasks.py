# tasks.py
from celery import Celery, shared_task
import requests
import time

app = Celery('webhook_tasks', broker='pyamqp://guest:guest@localhost:5672//')

@app.task(bind=True, max_retries=5)
@shared_task
def fire_webhook(self, company_id, url):
    try:
        print(company_id,url,"inside tasks")
        # Make HTTP GET request to the provided URL with headers
        response = requests.get(url)
        response.raise_for_status()

        return {"message": "Webhook request successful!"}

    except requests.RequestException as exc:
        # Handle HTTP request failure and retry using exponential backoff
        print(f"Webhook request failed: {exc}")
        retry_delay = 2 ** self.request.retries
        time.sleep(retry_delay)
        self.retry(exc=exc)

    except Exception as exc:
        # Handle other exceptions if needed
        print(f"An unexpected error occurred: {exc}")
        raise
