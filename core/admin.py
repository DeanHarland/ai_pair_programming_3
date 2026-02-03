from django.contrib import admin
from .models import Task, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'created_at']
    search_fields = ['name', 'description']
    list_per_page = 20


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'category', 'assigned_to', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'category', 'created_at', 'due_date']
    search_fields = ['title', 'description']
    list_editable = ['status', 'priority']
    date_hierarchy = 'created_at'
    list_per_page = 25
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Assignment & Priority', {
            'fields': ('assigned_to', 'status', 'priority')
        }),
        ('Dates', {
            'fields': ('due_date', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def save_model(self, request, obj, form, change):
        """Auto-set completed_at when status changes to completed"""
        if obj.status == 'completed' and not obj.completed_at:
            from django.utils import timezone
            obj.completed_at = timezone.now()
        super().save_model(request, obj, form, change)

