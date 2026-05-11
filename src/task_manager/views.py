from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import TemplateView

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
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.decorators.cache import cache_page
from django.core.cache import caches
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_not_required

from task_manager.tasks import add


# MTV
# @cache_page(60)
# @permission_required("task_manager.view_task")
# @transaction.atomic
# def tasks(request):
#
#     tasks = Tasks.objects.task_optimization()
#     paginator = Paginator(tasks, 50)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         "tasks": page_obj,
#         "page_obj": page_obj,
#     }
#     return render(request,"tasks.html",context=context)


# @method_decorator(login_not_required, name="dispatch")
class TasksView(ListView):
    template_name = "tasks.html"
    # login_url = "/account/login/"
    # permission_required = 'task_manager.view_task'
    model = Tasks
    paginate_by = 50
    paginator_class = Paginator
    queryset = Tasks.objects.task_optimization()

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        page_number = self.request.GET.get(self.page_kwarg)
        paginator = self.paginator_class(self.queryset,self.paginate_by)
        context["tasks"] = paginator.get_page(page_number)
        context["page_obj"] = paginator.get_page(page_number)
        return context


# def about(request):
#     return render(request,"about.html")


class AboutTemplateView(TemplateView):
    template_name = "about.html"


# def index_2(request):
#     return HttpResponse(f"<h1>Index 2. </h1>")


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Index 2. </h1>")


def user_test_validate(pk):

    res = add.delay(pk, pk + 1)
    print(res)
    return True


# @transaction.atomic
def user_tasks(request,pk):
    # user = User.objects.get(pk=pk)
    # task = user.tasks.get(id=3)
    #
    res = user_test_validate(pk)
    print(res)
    # task.priority = F("priority") + 1
    # if task.priority > 5:
    #     raise ValueError
    return HttpResponse(f"<h1>User </h1>")



@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


# def create_task_form(request):
#
#     if request.method == "POST":
#
#         form = TaskForm(request.POST)
#
#         if form.is_valid():
#
#             # Tasks.objects.create(
#             #     name=request.POST["name"],
#             #     priority=request.POST["priority"]
#             # )
#             # Tasks.objects.create(
#             #     name=request.cleaned_data.get("name"),
#             #     priority=request.cleaned_data.get("priority")
#             # )
#             form.save()
#             # caches["default"].clear()
#             return HttpResponseRedirect(reverse("tasks"))
#     else:
#         form = TaskForm()
#
#     return render(request, "task_form.html", {"form": form})



class TaskFormView(CreateView):
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks")




def create_attachment(request):

    if request.method == "POST":

        form = AttachmentsForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse("tasks"))
    else:
        form = AttachmentsForm()

    return render(request, "task_attachment.html", {"form": form})