from django.db import models



class TaskStatus(models.TextChoices):
    CREATED = "created"
    STARTED = "started"
    COMPLETED = "completed"
    CANCELED = "canceled"
    FAILED = "failed"