# Generated by Django 4.2.7 on 2023-11-24 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_tag_name_en_tag_name_ru_tag_name_uz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='view_co',
        ),
    ]