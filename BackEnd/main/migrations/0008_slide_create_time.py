# Generated by Django 5.1.1 on 2024-09-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
