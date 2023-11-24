from django.contrib import admin
from .models import Category, Tag, News, Social
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'user_id']
    prepopulated_fields = {'slug': ('title',), }

class SocialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Social, SocialAdmin)