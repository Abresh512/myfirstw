# Generated by Django 5.1.5 on 2025-01-21 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subject_student_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_subject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='app.registration'),
        ),
    ]
