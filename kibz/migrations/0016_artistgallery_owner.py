# Generated by Django 2.1.3 on 2018-11-29 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibz', '0015_artistgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistgallery',
            name='owner',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
