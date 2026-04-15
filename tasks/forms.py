from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task


class StyledFormMixin:
    def _apply_base_styles(self):
        for field in self.fields.values():
            existing = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing} form-control".strip()


class RegisterForm(StyledFormMixin, UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_base_styles()
        placeholders = {
            "username": "Choose a username",
            "email": "Enter your email",
            "password1": "Create a password",
            "password2": "Confirm your password",
        }
        for name, placeholder in placeholders.items():
            self.fields[name].widget.attrs["placeholder"] = placeholder

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class TaskForm(StyledFormMixin, forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    class Meta:
        model = Task
        fields = ["title", "description", "priority", "due_date", "completed"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Plan sprint review"}),
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Add notes, blockers, or the outcome you want.",
                }
            ),
            "priority": forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_base_styles()
        self.fields["completed"].widget.attrs["class"] = "form-check-input"
        self.fields["completed"].help_text = "Mark this task as finished."
        self.fields["title"].label = "Task title"
        self.fields["due_date"].label = "Due date"
