# Generated by Django 4.0 on 2022-01-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_alter_doctor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='info',
            field=models.JSONField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='more_info',
            field=models.JSONField(max_length=4000),
        ),
    ]