# Generated by Django 3.1 on 2020-10-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='catg',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
