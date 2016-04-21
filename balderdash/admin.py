from django.contrib import admin
from .models import Comments
from .models import Prompt

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user", "text")

class PromptAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "definition", "category")

admin.site.register(Prompt, PromptAdmin)
