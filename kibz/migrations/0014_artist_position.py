# Generated by Django 2.1.3 on 2018-11-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibz', '0013_auto_20181129_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='position',
            field=models.CharField(default='artist', max_length=100),
        ),
    ]
