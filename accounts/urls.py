from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit_view, name="profile_edit"),
    path("skills/", views.skill_list_view, name="skill_list"),
    path("skills/create", views.skill_create_view, name="skill_create"),
    path("skills/<int:skill_id>/edit/", views.skill_edit_view, name="skill_edit"),
    path("skills/<int:skill_id>/delete", views.skill_delete_view, name="skill_delete"),
]
