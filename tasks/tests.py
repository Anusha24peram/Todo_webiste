from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Task


class TaskViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="anush", password="strong-pass123")
        self.client.login(username="anush", password="strong-pass123")

    def test_add_task_creates_record_for_logged_in_user(self):
        response = self.client.post(
            reverse("add_task"),
            {
                "title": "Ship portfolio update",
                "description": "Refresh the landing page copy",
                "priority": "H",
                "due_date": "2026-04-15T10:30",
                "completed": "",
            },
        )

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().user, self.user)

    def test_toggle_task_switches_completion_state(self):
        task = Task.objects.create(
            user=self.user,
            title="Prepare sprint notes",
            priority="M",
            due_date=timezone.now(),
        )

        response = self.client.post(reverse("toggle_task", args=[task.id]))

        self.assertRedirects(response, reverse("home"))
        task.refresh_from_db()
        self.assertTrue(task.completed)

    def test_home_filters_pending_tasks(self):
        Task.objects.create(user=self.user, title="Done item", completed=True, priority="L")
        Task.objects.create(user=self.user, title="Open item", completed=False, priority="H")

        response = self.client.get(reverse("home"), {"status": "pending"})

        self.assertContains(response, "Open item")
        self.assertNotContains(response, "Done item")
