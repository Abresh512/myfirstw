# Generated by Django 5.1.5 on 2025-03-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_subj_teach_section_alter_class_leader_grade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Male', models.CharField(blank=True, max_length=50, null=True)),
                ('Female', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='class_leader',
            name='grade',
            field=models.CharField(blank=True, choices=[('grade_9', '9'), ('grade_10', '10')], default=False, max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='registration',
            name='gender',
        ),
        migrations.AlterField(
            model_name='registration',
            name='grade',
            field=models.CharField(choices=[('grade_9', '9'), ('grade_10', '10')], default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='section',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default=False, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='student_subject',
            name='grade',
            field=models.CharField(blank=True, choices=[('grade_9', '9'), ('grade_10', '10')], default=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='subj_teach',
            name='grade',
            field=models.CharField(blank=True, choices=[('grade_9', '9'), ('grade_10', '10')], default=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='subj_teach',
            name='section',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.ManyToManyField(null=True, related_name='gender', to='app.gender'),
        ),
    ]
