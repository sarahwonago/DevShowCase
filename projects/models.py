from django.db import models
from django.contrib.auth import get_user_model

CustomUser= get_user_model()


class Profession(models.Model):

    class Meta:
        verbose_name_plural = "Profession"
        ordering = ["-created_at"]

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Technology(models.Model):

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ["-created_at"]

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    class Meta:
        verbose_name_plural = "Profile"

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    profile_photo = models.ImageField(default="profile.png", upload_to="profile/")
    profession = models.ManyToManyField(Profession)
    tech_stack = models.ManyToManyField(Technology)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    class Meta:
        verbose_name_plural = "Follow"
        ordering = ["-created_at"]

    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="following")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower.username

class ProfileLikes(models.Model):
    class Meta:
        verbose_name_plural = "ProfileLikes"
        ordering = ["-created_at"]

    liker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="liked_profiles")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.liker.username

    
class Project(models.Model):
    class Meta:
        verbose_name_plural = "Projects"
        ordering = ["-created_at"]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    technology_used = models.ManyToManyField(Technology)
    description = models.TextField()
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    pro_image = models.ImageField(upload_to="project/", default="project.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name
    
class ProjectLikes(models.Model):
    class Meta:
        verbose_name_plural = "ProjectLikes"
        ordering = ["-created_at"]

    project_liker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="liked_projects")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_liker.username
    
class ProjectComment(models.Model):
    class Meta:
        verbose_name_plural = "ProjectComments"
        ordering = ["-created_at"]

    project_commentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="commented_projects")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_commentor.username
    
class ProjectImage(models.Model):
    class Meta:
        verbose_name_plural = "ProjectImages"
        ordering = ["-created_at"]

    image = models.ImageField(upload_to='project/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name