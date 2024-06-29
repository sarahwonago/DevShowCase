from django.db import models
from django.contrib.auth import get_user_model

CustomUser= get_user_model()


class Profile(models.Model):
    class Meta:
        verbose_plural_name = "Profile"

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
    profile_photo = models.ImageField(default="profile.png", upload_to="profile/")
    profession = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username


class Follow(models.Model):
    class Meta:
        verbose_plural_name = "Follow"

    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="following")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="followers")

    def __str__(self):
        return self.follower.username

class ProfileLikes(models.Model):
    class Meta:
        verbose_plural_name = "ProfileLikes"

    liker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="liked_profiles")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return self.liker.username
    
class Technology(models.Model):

    class Meta:
        verbose_plural_name = "Technologies"

    name = models.CharField(max_length=255)

    
class Project(models.Model):
    class Meta:
        verbose_plural_name = "Projects"

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    technology_used = models.ManyToManyField(Technology)
    description = models.TextField()
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
   
    def __str__(self):
        return self.name
    
class ProjectLikes(models.Model):
    class Meta:
        verbose_plural_name = "ProjectLikes"

    project_liker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="liked_projects")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="likes")

    def __str__(self):
        return self.project_liker.username
    
class ProjectComment(models.Model):
    class Meta:
        verbose_plural_name = "ProjectComments"

    project_commentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="commented_projects")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.project_commentor.username
    
class ProjectImage(models.Model):
    class Meta:
        verbose_plural_name = "ProjectImages"

    image = models.ImageField(upload_to='project_images/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.project.name