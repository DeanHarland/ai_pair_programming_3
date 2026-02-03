from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    """Form for creating and updating tasks"""
    
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }
        ),
        required=False,
        label='Due Date',
    )
    
    class Meta:
        model = Task
        fields = ['title', 'category', 'due_date']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter task title',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }
        labels = {
            'title': 'Task Title',
            'category': 'Category',
            'due_date': 'Due Date',
        }
