from django.contrib import admin

from blogengine import models
from .models_admin import PostAdmin

admin.site.register(models.Category)
admin.site.register(models.Post, PostAdmin)
