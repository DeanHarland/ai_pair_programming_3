from django.shortcuts import render
from django.db.models import Q
from .models import Task


def index(request):
    """Display all tasks sorted by due date"""
    # Fetch pending tasks (pending or in_progress) sorted by due date
    pending_tasks = Task.objects.filter(
        status__in=['pending', 'in_progress']
    ).order_by('due_date').select_related('category', 'assigned_to')
    
    # Fetch completed tasks sorted by completed date (most recent first)
    completed_tasks = Task.objects.filter(
        status='completed'
    ).order_by('-completed_at').select_related('category', 'assigned_to')
    
    context = {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'index.html', context)

