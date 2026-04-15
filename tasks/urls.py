from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_task, name="add_task"),
    path("edit/<int:id>/", views.edit_task, name="edit_task"),
    path("toggle/<int:id>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:id>/", views.delete_task, name="delete_task"),
    path("register/", views.register, name="register"),
]
