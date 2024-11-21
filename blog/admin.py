from django.contrib import admin
from .models import Blog


# Register your models here.
@admin.register(Blog)
class BlogEntryAdmin(admin.ModelAdmin):
    """Настройки отображения модели в админке"""

    list_display = ("title", "short_content", "created_at", "is_published", "view_count")  # колонки
    search_fields = ("title", "content")  # поиск по полям

    def short_content(self, obj):
        """Обрезает текст если он больше 50 символов."""
        if len(obj.content) > 50:
            return obj.content[:50] + '...'
        return obj.content
    short_content.short_description = 'content'
