# Generated by Django 4.1.4 on 2022-12-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0010_alter_movie_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Men'), ('F', 'Woman')], default='M', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='orm_app.actor'),
        ),
    ]
