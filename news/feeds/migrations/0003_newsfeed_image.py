# Generated by Django 3.1 on 2020-10-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_auto_20201027_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
