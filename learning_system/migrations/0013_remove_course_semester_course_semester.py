# Generated by Django 4.2.7 on 2024-04-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0012_remove_course_semester_course_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(default=1, verbose_name={1: 'first', 2: 'second'}),
            preserve_default=False,
        ),
    ]
