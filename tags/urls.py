from django.urls import path
from . import views

urlpatterns = [
    path("", views.tag_list, name="tag_list"),
    path("create/", views.tag_create, name="tag_create"),
    path("<int:pk>/edit/", views.tag_update, name="tag_update"),
    path("<int:pk>/delete/", views.tag_delete_confirmation, name="tag_delete_confirmation"),
    path("<int:pk>/delete/confirm/", views.tag_delete, name="tag_delete"),
]