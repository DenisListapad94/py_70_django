from django.shortcuts import render

from django.http import HttpResponse
from task_manager.models import Tasks

# MTV
def tasks(request):

    context = {
        "tasks": Tasks.objects.all()
    }
    return render(request,"tasks.html",context=context)


def about(request):
    return render(request,"about.html")


def index_2(request,task):
    return HttpResponse(f"<h1>Index 2. {task}</h1>")