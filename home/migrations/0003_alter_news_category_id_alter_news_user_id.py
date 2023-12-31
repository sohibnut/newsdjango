# Generated by Django 4.2.7 on 2023-11-17 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_news_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='home.category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to=settings.AUTH_USER_MODEL),
        ),
    ]
