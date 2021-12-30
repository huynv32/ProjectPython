from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, News,Image_News

# Register your models here.

admin.site.register(Image_News)
admin.site.register(Category)
admin.site.register(News)
