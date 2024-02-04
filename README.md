# Webhook-Subscription-API
An API for managing webhooks. It includes features for creating, listing, retrieving, updating, and deleting webhooks. Additionally, it allows firing events to active webhooks using Celery tasks.

## Prerequisites
Before running the project, make sure you have the following installed:

- Python (3.8 or higher)
- Django
- Celery
- RabbitMQ (for Celery)

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/gauravmittal54/Webhook-Subscription-API.git
   
2. **Install dependencies & Run migrations:**
   ```bash
   pip install django celery requests djangorestframework
   python manage.py makemigrations
   python manage.py migrate
   
3. **Start Celery worker (make sure RabbitMQ is running):**
   ```bash
   celery -A webhookServiceApi.tasks worker --loglevel=info

3. **Start the Django development server:**
   ```bash
   python manage.py runserver

## API Endpoints
1.Create Webhook:
  POST /webhooks/

2.List Webhooks:
  GET /webhooks/all/

3.Retrieve Webhook:
  GET /webhooks/<uuid:_id>/

4.Fire Event:
  POST /fire-event/

5.Update Webhook:
  PUT /webhooks/<uuid:_id>/update/

6.Delete Webhook:
  DELETE /webhooks/<uuid:_id>/delete/

## Models
### WebhookEvent
- _id: UUIDField (Primary Key)
- company_id: CharField
- url: URLField (Unique)
- headers: JSONField (Optional)
- events: JSONField
- is_active: BooleanField (Default: True)
- created_at: DateTimeField
- updated_at: DateTimeField (Auto-updated)
