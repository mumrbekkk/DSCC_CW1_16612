from django.contrib import admin

from apps.users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "date_joined",
    )

    search_fields = ("username", "email", "first_name", "last_name")

    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
        "groups",
    )

    ordering = ("-date_joined",)
