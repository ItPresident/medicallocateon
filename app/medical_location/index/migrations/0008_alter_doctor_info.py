# Generated by Django 4.0 on 2022-01-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_town_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='info',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
