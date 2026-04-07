from django import forms
from django.forms import  Textarea
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError

from task_manager.models import Tasks, Attachments


def validate_max_count_split(value):
    if len(value.split()) > 4:
        raise ValidationError("%(value)s is too long. It must be less than 4 parts",
            params={"value": value},
        )

# class TaskForm(forms.Form):
#     name = forms.CharField(
#         label="наименование задачи",
#         max_length=100,
#         validators = [
#             validate_max_count_split,
#         ]
#     )
#     priority = forms.IntegerField(
#         label="приоритет",
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(5),
#         ]
#     )
#     description = forms.CharField(
#         required=False,
#         label="Описание",
#         widget=forms.Textarea(
#             attrs={
#                 "wid": "30",
#                 "class": "special"
#             }
#         )
#     )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["name","priority","description"]
        widgets = {
            "description": Textarea(attrs={"cols": 50, "rows": 5}),
        }

class AttachmentsForm(forms.ModelForm):
    class Meta:
        model = Attachments
        fields = ["name","photo","task"]
