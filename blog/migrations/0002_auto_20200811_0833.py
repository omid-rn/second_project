# Generated by Django 3.0.8 on 2020-08-11 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]