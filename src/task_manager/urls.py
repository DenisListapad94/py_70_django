
from django.urls import path, re_path,include
from task_manager.views import TasksView,MyView,AboutTemplateView,TaskFormView,user_tasks,create_attachment
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('', cache_page(60)(TasksView.as_view()), name="tasks"),
    path('about', AboutTemplateView.as_view(), name="about"),
    path('users/<int:pk>', user_tasks, name="user_tasks"),
    re_path("details/", MyView.as_view()),
    path("create",TaskFormView.as_view(),name="create_task"),
    path("create_attachment",create_attachment,name="create_attachment"),
    path("api/",include("task_manager.v1.urls")),
]
