from django.contrib import admin
from .models import Character

# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'true_name', 'is_corrupted')
    list_filter = ('species', 'is_corrupted')
    search_fields = ('name', 'true_name', 'malnomen')
