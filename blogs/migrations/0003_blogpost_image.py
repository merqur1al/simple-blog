# Generated by Django 3.0.7 on 2020-09-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
