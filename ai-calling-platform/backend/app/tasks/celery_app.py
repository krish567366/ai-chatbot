from celery import Celery
from app.settings import settings

celery = Celery(
	"ai_calling",
	broker=settings.REDIS_URL,
	backend=settings.REDIS_URL,
	include=["app.tasks.jobs"],
)