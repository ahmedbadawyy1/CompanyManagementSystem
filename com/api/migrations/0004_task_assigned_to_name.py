# Generated by Django 4.2.13 on 2024-07-09 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_employees_project_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_to_name',
            field=models.CharField(default=1, max_length=200, verbose_name='emp_name'),
            preserve_default=False,
        ),
    ]
