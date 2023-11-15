from django.contrib import admin
from .models import Category, Tag, News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'view_co', 'user_id']
    readonly_fields = ['view_co']
    prepopulated_fields = {'slug': ('title',), }

admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)