# Generated by Django 5.1.1 on 2024-09-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
