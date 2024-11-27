from django.contrib import admin
from .models import CustomUser
from .models import Prompt
admin.site.register(CustomUser)

# Register your models here.


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ('user_prompt', 'bot_response', 'created_at')
    search_fields = ('user_prompt', 'bot_response')
