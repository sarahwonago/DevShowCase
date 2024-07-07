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
    else:
        form = CustomUserCreationForm()

    context = {
        "form":form,
    }
    return render(request, "users/signup.html", context)

def update_user_view(request):
    user= request.user
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("core:home")
    
    else:
        form = CustomUserChangeForm(instance=user)
        
    context ={
        "form":form,
    }

    return render(request, "users/update_user.html", context)

def logout_view(request):
    logout(request)
    return redirect("login")