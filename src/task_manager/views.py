from django.core.paginator import Paginator
from django.http import HttpResponse
from task_manager.models import Tasks
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db import transaction
from django.urls import reverse
from task_manager.forms import TaskForm, AttachmentsForm
from django.core.signals import request_finished
from django.dispatch import receiver
from account.models import User
from django.db.models import F




# MTV
@transaction.atomic
def tasks(request):
    tasks = Tasks.objects.task_optimization()
    paginator = Paginator(tasks, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "tasks": page_obj,
        "page_obj": page_obj,
    }
    return render(request,"tasks.html",context=context)


def about(request):
    return render(request,"about.html")


def index_2(request,task):
    return HttpResponse(f"<h1>Index 2. {task}</h1>")

@transaction.atomic
def user_tasks(request,pk):
    user = User.objects.get(pk=pk)
    task = user.tasks.get(id=3)

    task.priority = F("priority") + 1
    import pdb;pdb.set_trace()
    if task.priority > 5:
        raise ValueError
    return HttpResponse(f"<h1>User {user.email}</h1>")



@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


def create_task_form(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            # Tasks.objects.create(
            #     name=request.POST["name"],
            #     priority=request.POST["priority"]
            # )
            # Tasks.objects.create(
            #     name=request.cleaned_data.get("name"),
            #     priority=request.cleaned_data.get("priority")
            # )
            form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = TaskForm()

    return render(request, "task_form.html", {"form": form})


def create_attachment(request):

    if request.method == "POST":

        form = AttachmentsForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = AttachmentsForm()

    return render(request, "task_attachment.html", {"form": form})