# Generated by Django 4.2.7 on 2024-04-30 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0014_delete_semester_rename_degree_id_course_degree_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='degree',
        ),
        migrations.AddField(
            model_name='course',
            name='degree',
            field=models.ForeignKey(default='CEIT', on_delete=django.db.models.deletion.CASCADE, to='learning_system.degreeprogram'),
            preserve_default=False,
        ),
    ]
