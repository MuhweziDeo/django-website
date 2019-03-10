from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.TeamProfile)
admin.site.register(models.Artist)
admin.site.register(models.Client)
admin.site.register(models.CompanyGallery)
admin.site.register(models.Video)
