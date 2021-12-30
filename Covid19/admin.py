from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Country,Summary,Global

# Register your models here.

admin.site.register(Summary)
admin.site.register(Country)
admin.site.register(Global)
