from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    form = CustomUserCreationForm()
    context = {
        "form":form,
    }
    return render(request, "users/signup.html", context)
