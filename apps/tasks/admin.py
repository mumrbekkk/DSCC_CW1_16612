from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "project",
        "is_completed",
        "tag_list",
        "created_at",
    )

    list_filter = (
        "is_completed",
        "project",
        "tags",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "project__name",
    )

    autocomplete_fields = ("project", "tags")

    ordering = ("-created_at",)

    list_select_related = ("project",)

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tag_list.short_description = "Tags"
