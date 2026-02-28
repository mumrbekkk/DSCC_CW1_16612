from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from projects.models import Project
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk, owner=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            form.save_m2m()
            return redirect("project_detail", pk=project.pk)
    else:
        form = TaskForm()

    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_update(request, project_pk, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect("project_detail", pk=project_pk)

    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_delete_confirmation(request, project_pk, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


@login_required
@require_POST
def task_delete(request, project_pk, pk):
    task = get_object_or_404(Task, pk=pk, project__owner=request.user)
    task.delete()
    return redirect("project_detail", pk=project_pk)



