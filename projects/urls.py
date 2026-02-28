from django.urls import path
from . import views
from tasks import views as task_views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("create/", views.project_create, name="project_create"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("<int:pk>/edit/", views.project_update, name="project_update"),
    path("<int:pk>/delete/", views.project_delete_confirmation, name="project_delete_confirmation"),
    path("<int:pk>/delete/confirm/", views.project_delete, name="project_delete"),

    path("<int:project_pk>/tasks/create/", task_views.task_create, name="task_create"),
    path("<int:project_pk>/tasks/<int:pk>/edit/", task_views.task_update, name="task_update"),
    path("<int:project_pk>/tasks/<int:pk>/delete/", task_views.task_delete_confirmation, name="task_delete_confirmation"),
    path("<int:project_pk>/tasks/<int:pk>/delete/confirm/", task_views.task_delete, name="task_delete"),
]