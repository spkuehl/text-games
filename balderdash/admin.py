from django.contrib import admin

from .models import Prompt

class PromptAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "definition", "category")

admin.site.register(Prompt, PromptAdmin)
