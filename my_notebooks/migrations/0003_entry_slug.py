# Generated by Django 4.1.4 on 2022-12-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_notebooks', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
