# Generated by Django 3.2.25 on 2024-05-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_system', '0015_remove_course_degree_course_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastpaper',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
