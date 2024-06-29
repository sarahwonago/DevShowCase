from django.contrib import admin

from .models import *

admin.site.register(Profile)
admin.site.register(ProfileLikes)
admin.site.register(Follow)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(ProjectLikes)
admin.site.register(ProjectImage)
admin.site.register(ProjectComment)