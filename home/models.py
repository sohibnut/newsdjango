from django.db import models
from .manager import BaseModel
from django.contrib.auth.models import User

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='news/')
    view_co = models.BigIntegerField(default=0)
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='news')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    tag_id = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title

