# Generated by Django 5.0.7 on 2024-07-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]