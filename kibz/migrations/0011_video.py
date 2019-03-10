# Generated by Django 2.1.3 on 2018-11-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibz', '0010_companygallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_1', models.URLField()),
                ('video_2', models.URLField()),
                ('video_3', models.URLField()),
            ],
        ),
    ]
