
from django.urls import path, re_path
from task_manager.views import tasks,index_2,about,create_task_form,user_tasks,create_attachment

urlpatterns = [
    path('', tasks, name="tasks"),
    path('about', about, name="about"),
    path('users/<int:pk>', user_tasks, name="user_tasks"),
    re_path(r"^details/(?P<task>[0-9]{4})/$", index_2),
    path("create",create_task_form,name="create_task"),
    path("create_attachment",create_attachment,name="create_attachment"),

]
