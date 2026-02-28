from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from common.auth.superuser_required import superuser_required
from .models import Tag
from .forms import TagForm


@superuser_required
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tags/tag_list.html", {"tags": tags})


@superuser_required
def tag_create(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("tag_list")
    return render(request, "tags/tag_form.html", {"form": form})


@superuser_required
def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        form.save()
        return redirect("tag_list")
    return render(request, "tags/tag_form.html", {"form": form})


@superuser_required
def tag_delete_confirmation(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, "tags/tag_confirm_delete.html", {"tag": tag})


@superuser_required
@require_POST
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect("tag_list")