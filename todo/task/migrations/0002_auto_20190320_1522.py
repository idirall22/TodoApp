# Generated by Django 2.1.7 on 2019-03-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='tasks',
            field=models.ManyToManyField(to='task.Task'),
        ),
    ]
