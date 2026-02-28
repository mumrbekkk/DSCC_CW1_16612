from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Project
from .forms import ProjectForm


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    return render(request, "projects/project_list.html", {"projects": projects})


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/project_form.html", {"form": form})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    return render(request, "projects/project_detail.html", {"project": project})


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect("project_list")
    return render(request, "projects/project_form.html", {"form": form})


@login_required
def project_delete_confirmation(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    return render(
        request,
        "projects/project_confirm_delete.html",
        {"project": project},
    )


@login_required
@require_POST
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    project.delete()
    return redirect("project_list")
