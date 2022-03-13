# Generated by Django 4.0 on 2022-01-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_alter_doctor_more_info_alter_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(max_length=255, upload_to='doctor_photo/%Y/%m/%d/'),
        ),
    ]