from django import forms
from django.urls import reverse

from todo_list.models import ToDoItem


class ToDoItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("title", "description")

        widgets = {
            "description": forms.Textarea(attrs={"cols": 30, "rows": 5}),
        }
        help_texts = {
            "descriptions": "Some useful help text."
        }
