from django.urls import path
from .views import *

app_name="core"

urlpatterns = [
    path("user_profile/<int:pk>/", user_profile_view, name="user-profile"),
    path("add_project/", add_project_view, name="add-project"),
    path("profile_update/", profile_update_view, name="profile-update"),
    path("my_profile/", my_profile_view, name="my-profile"),
    path("", home_view, name="home"),
]