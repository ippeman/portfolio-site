# Generated by Django 2.2.28 on 2022-06-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_todo_checkbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.TextField()),
                ('proficiency', models.TextField()),
            ],
        ),
    ]
