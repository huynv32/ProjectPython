from django.contrib import admin
from .models import Category, Answer, Question, Result

# Register your models here.

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
