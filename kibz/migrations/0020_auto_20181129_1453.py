# Generated by Django 2.1.3 on 2018-11-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibz', '0019_auto_20181129_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_2',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_3',
            field=models.CharField(max_length=500),
        ),
    ]
