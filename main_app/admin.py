from django.contrib import admin
# Model import
from .models import Post, Work

# Register your models here.
admin.site.register(Post)
admin.site.register(Work)