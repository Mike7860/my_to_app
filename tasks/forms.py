from django import forms
from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'body', 'due_date', 'deadline', 'category')


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('body', 'due_date', 'deadline', 'task_finished', 'category')