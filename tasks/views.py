from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import RegisterForm, TaskForm
from .models import Task


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account is ready. Welcome aboard.")
        return redirect("home")

    return render(request, "tasks/register.html", {"form": form})


@login_required
def home(request):
    query = request.GET.get("q", "").strip()
    status_filter = request.GET.get("status", "all")
    priority_filter = request.GET.get("priority", "all")
    sort = request.GET.get("sort", "due_date")

    tasks = Task.objects.filter(user=request.user)

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if status_filter == "completed":
        tasks = tasks.filter(completed=True)
    elif status_filter == "pending":
        tasks = tasks.filter(completed=False)
    elif status_filter == "overdue":
        tasks = tasks.filter(completed=False, due_date__lt=timezone.now())

    if priority_filter in {"H", "M", "L"}:
        tasks = tasks.filter(priority=priority_filter)

    sort_options = {
        "due_date": ["due_date", "completed", "-created_at"],
        "priority": ["priority", "completed", "due_date"],
        "recent": ["-created_at"],
        "title": ["title"],
    }
    tasks = tasks.order_by(*sort_options.get(sort, sort_options["due_date"]))

    all_tasks = Task.objects.filter(user=request.user)
    now = timezone.now()
    stats = {
        "total": all_tasks.count(),
        "completed": all_tasks.filter(completed=True).count(),
        "pending": all_tasks.filter(completed=False).count(),
        "overdue": all_tasks.filter(completed=False, due_date__lt=now).count(),
    }
    stats["completion_rate"] = (
        round((stats["completed"] / stats["total"]) * 100) if stats["total"] else 0
    )

    context = {
        "tasks": tasks,
        "task_form": TaskForm(),
        "query": query,
        "status_filter": status_filter,
        "priority_filter": priority_filter,
        "sort": sort,
        "stats": stats,
        "now": now,
    }
    return render(request, "tasks/home.html", context)


@login_required
def add_task(request):
    form = TaskForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, f'"{task.title}" was added successfully.')
            return redirect("home")

        messages.error(request, "Please correct the form errors and try again.")

    return render(request, "tasks/add.html", {"form": form})


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    form = TaskForm(request.POST or None, instance=task)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f'"{task.title}" was updated.')
        return redirect("home")

    return render(request, "tasks/edit.html", {"form": form, "task": task})


@login_required
@require_POST
def toggle_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    state = "completed" if task.completed else "marked as active"
    messages.success(request, f'"{task.title}" was {state}.')
    return redirect("home")


@login_required
@require_POST
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    title = task.title
    task.delete()
    messages.success(request, f'"{title}" was deleted.')
    return redirect("home")
