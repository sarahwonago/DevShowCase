from django.urls import path
from .views import *

app_name="core"

urlpatterns = [
    path("user-profile/<int:pk>/", user_profile_view, name="user-profile"),
    path("projects/<int:pk>/", detail_project_view, name="detail-project"),
    path("add-project/", add_project_view, name="add-project"),
    path("profile-update/", profile_update_view, name="profile-update"),
    path("my-profile/", my_profile_view, name="my-profile"),
    path("", home_view, name="home"),
]