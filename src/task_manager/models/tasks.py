from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from config.models import BaseModel
from task_manager.constants import TaskStatus
from task_manager.managers import TaskManager




class Tasks(BaseModel):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name = "Наименование"
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    status = models.CharField(
        choices=TaskStatus,
        default=TaskStatus.CREATED,
        verbose_name="Статус"
    )
    priority = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        default=3,
        verbose_name="Приоритетность"
    )
    is_reopened = models.BooleanField(
        default=False,
        verbose_name="Переоткрывалась ли"
    )

    project = models.ForeignKey(
        to = "Projects",
        related_name="tasks",
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )

    assignee = models.ForeignKey(
        to="account.User",
        related_name="tasks",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    objects = TaskManager()

    class Meta:
        ordering = ["-created_at"]
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.name



class EducationTasks(Tasks):
    class Meta:
        proxy = True


