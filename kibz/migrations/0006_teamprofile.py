# Generated by Django 2.1.2 on 2018-11-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibz', '0005_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('profile', models.ImageField(upload_to='profile_images')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
                ('created_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
