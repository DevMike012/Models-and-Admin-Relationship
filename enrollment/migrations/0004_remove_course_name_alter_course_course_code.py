# Generated by Django 5.1.4 on 2025-01-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0003_course_course_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=100, verbose_name='Course code'),
        ),
    ]
