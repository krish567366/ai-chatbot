from app.tasks.celery_app import celery


@celery.task
def add(x: int, y: int) -> int:
	return x + y