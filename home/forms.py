from django import forms    
from .models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'title_en', 'title_uz', 'title_ru', 'image', 'body', 'body_en', 'body_uz', 'body_ru', 'category_id', 'tag_id']