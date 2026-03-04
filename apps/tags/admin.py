from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "task_count",
    )

    search_fields = ("name",)

    ordering = ("name",)

    def task_count(self, obj):
        return obj.tasks.count()

    task_count.short_description = "Tasks using this tag"