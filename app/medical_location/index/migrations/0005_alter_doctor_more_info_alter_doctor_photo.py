# Generated by Django 4.0 on 2022-01-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_worckplace_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='more_info',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(upload_to='doctor_photo/%Y/%m/%d/'),
        ),
    ]
