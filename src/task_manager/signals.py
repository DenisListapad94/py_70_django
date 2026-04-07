from django.db.models.signals import post_save
from django.dispatch import receiver
from task_manager.models import Tasks
from account.models import User


@receiver(post_save, sender=Tasks)
def my_test_signal(sender,instance,created, **kwargs):
    user = User.objects.get(id=1)
    instance.assignee = user
    # instance.save()