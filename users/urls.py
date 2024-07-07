from django.urls import path
from .views import *

app_name="users"

urlpatterns =[
    path("update_user/", update_user_view, name="update-user"),
    path("logout_user/", logout_view, name="logout-user"),
    path("", signup_view, name="signup"),
]