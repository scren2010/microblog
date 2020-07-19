from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# Register your models here.
from app.models import Post


class PostAdmin(MPTTModelAdmin):
    """Сообщения"""
    list_display = ("id", "user", "text", "parent", "like", "date")
    mptt_level_indent = 20

admin.site.register(Post, PostAdmin)