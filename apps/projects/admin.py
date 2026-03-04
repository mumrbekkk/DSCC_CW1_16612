from django.contrib import admin
from .models import Project
from apps.tasks.models import Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    fields = ("title", "is_completed", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "created_at",
        "task_count",
    )

    search_fields = (
        "name",
        "description",
        "owner__username",
    )

    list_filter = (
        "created_at",
        "owner",
    )

    inlines = [TaskInline]

    ordering = ("-created_at",)

    def task_count(self, obj):
        return obj.tasks.count()

    task_count.short_description = "Tasks"