from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q


from projects.models import *
from .forms import *

CustomUser=get_user_model()

@login_required
def home_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    #followers for my profile
    followers= Follow.objects.filter(profile=profile)
    #the profiles that the  user is following
    following = Follow.objects.filter(follower=user)

    #list of users folliwing me
    my_followers = []
    for my_follower in followers:
        my_followers.append(my_follower.follower)

    #list of profiles i am following
    my_followings = []
    for my_following in following:
        my_followings.append(my_following.profile)

    projects = Project.objects.filter(Q(profile__user__in = my_followers)| Q(profile__in = my_followings)|Q(profile=profile))
    context = {
        "projects":projects,
    }
    return render(request, "core/home.html", context)

@login_required
def my_profile_view(request):
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    followers= Follow.objects.filter(profile=user_profile)
    following = Follow.objects.filter(follower=user)

    if followers:
        profile_followers= followers.count
    else:
        profile_followers=0

    if following:
        profile_following= following.count
    else:
        profile_following=0
    context={
        "profile":user_profile,
        "followers": profile_followers,
        "following":profile_following,
    }
    return render(request, "core/my_profile.html", context)

@login_required
def user_profile_view(request, pk):
    user = request.user

    requested_profile = get_object_or_404(Profile, id=pk)
    requested_profile_user = get_object_or_404(CustomUser, profile=requested_profile)

    #followers for requested profile
    followers= Follow.objects.filter(profile=requested_profile)
    #the profiles that the requested user is folloewing
    following = Follow.objects.filter(follower=requested_profile_user)

    #the profiles that the current logged in user is following
    logged_in_user_following = Follow.objects.filter(follower=user)
    

    flw=[]

    for followedprofile in logged_in_user_following:
        flw.append(followedprofile.profile)

    #btn follow unfollow text
    if requested_profile in flw:
            btn_text = 'UNFOLLOW'
            
    else:
            btn_text='FOLLOW'

    #follow/unfollowing
    if request.method == 'POST':
        if requested_profile in flw:
            followed_profile = Follow.objects.get(follower=user, profile=requested_profile)
            followed_profile.delete()
            
        else:
            new_followed_profile = Follow.objects.create(follower=user, profile=requested_profile)
            new_followed_profile.save()
            
        return redirect(f"/user_profile/{pk}/")
      

    if followers:
        profile_followers= followers.count
    else:
        profile_followers=0

    if following:
        profile_following= following.count
    else:
        profile_following=0

    context={
        "profile":requested_profile,
        "followers": profile_followers,
        "following":profile_following,
        "btn_text":btn_text,
    }
    return render(request, "core/user_profile.html", context)



@login_required
def profile_update_view(request):   
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("core:my-profile")

    else:
        form = ProfileForm(instance=user_profile)

    context = {
        "form":form,
    }
    return render(request, "core/update_profile.html", context)

@login_required
def add_project_view(request):
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)
    
    if request.method=='POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile=user_profile
            project.save()
            return redirect("core:home")

    else:
        form= ProjectForm()

    context = {
        "form":form,
    }
    return render(request, "core/add_project.html", context)


