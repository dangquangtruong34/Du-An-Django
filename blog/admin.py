from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'created_at',
    )
    search_fields = ('title',)

admin.site.register(Blog, BlogAdmin)