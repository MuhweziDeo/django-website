# Generated by Django 2.1.3 on 2018-11-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibz', '0011_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile_photo',
            field=models.ImageField(blank='True', default=None, upload_to='artist_profile'),
        ),
    ]
