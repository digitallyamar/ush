from django.contrib import admin
from .models import Shortener

# Register your models here.

@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in 
    Shortener._meta.get_fields()]