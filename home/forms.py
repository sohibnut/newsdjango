from django import forms    
from .models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image', 'body', 'category_id', 'tag_id']