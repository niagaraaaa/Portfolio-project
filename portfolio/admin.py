from django.contrib import admin
from .models import Contact,Category,Blog, Team, ProtCategory, Portfolio

# Register your models here.

admin.site.register((Contact,Category,Blog, Team, ProtCategory, Portfolio)) 
