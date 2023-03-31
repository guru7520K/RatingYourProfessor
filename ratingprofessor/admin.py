from django.contrib import admin

# Register your models here.
from .models import Professor,Rating
# Register your models here.
admin.site.register(Professor)
admin.site.register(Rating)
