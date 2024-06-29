from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import logout
from projects.models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            return redirect("login")

    form = CustomUserCreationForm()
    context = {
        "form":form,
    }
    return render(request, "users/signup.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")