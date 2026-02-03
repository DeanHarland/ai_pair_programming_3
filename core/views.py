from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Task
from .forms import TaskForm


def index(request):
    """Display all tasks and handle new task creation"""
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = 'pending'
            task.priority = 'medium'  # Default priority
            task.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('core:index')
    else:
        form = TaskForm()
    
    # Fetch pending tasks (pending or in_progress) sorted by due date
    pending_tasks = Task.objects.filter(
        status__in=['pending', 'in_progress']
    ).order_by('due_date').select_related('category', 'assigned_to')
    
    # Fetch completed tasks sorted by completed date (most recent first)
    completed_tasks = Task.objects.filter(
        status='completed'
    ).order_by('-completed_at').select_related('category', 'assigned_to')
    
    context = {
        'form': form,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'index.html', context)


