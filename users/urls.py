from django.urls import path
from .views import *

urlpatterns =[
    path("logout_user/", logout_view, name="logout-user"),
    path("", signup_view, name="signup"),
]