
from django.urls import path, re_path
from task_manager.views import index,index_2,about

urlpatterns = [
    path('', index, name="tasks"),
    path('about', about, name="about"),
    re_path(r"^details/(?P<task>[0-9]{4})/$", index_2),
]
