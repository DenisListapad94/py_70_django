
from django.http import HttpResponse
from task_manager.models import Tasks
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from task_manager.forms import TaskForm
from django.core.signals import request_finished
from django.dispatch import receiver




# MTV
@receiver(request_finished)
def tasks(sender, **kwargs):
    print("Request finished!")
    context = {
        "tasks": Tasks.objects.select_related("assignee").prefetch_related("tags","comments").all()
    }
    return render(sender,"tasks.html",context=context)


def about(request):
    return render(request,"about.html")


def index_2(request,task):
    return HttpResponse(f"<h1>Index 2. {task}</h1>")




@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


def create_task_form(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            # Tasks.objects.create(
            #     name=request.POST["name"],
            #     priority=request.POST["priority"]
            # )
            # Tasks.objects.create(
            #     name=request.cleaned_data.get("name"),
            #     priority=request.cleaned_data.get("priority")
            # )
            # form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = TaskForm()

    return render(request, "task_form.html", {"form": form})