from modeltranslation.translator import TranslationOptions, register
from .models import News, Category, Tag

@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'body', )

@register(Tag)
class TagsTranslation(TranslationOptions):
    fields = ('name',)
