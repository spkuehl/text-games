from django.contrib import admin

from .models import Prompt, UserDefinition

class PromptAdmin(admin.ModelAdmin):
    list_display = ("id", "word", "definition", "category")


class UserDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'user_name', 'prompt', 'user_definition')

admin.site.register(Prompt, PromptAdmin)
admin.site.register(UserDefinition, UserDefinitionAdmin)
