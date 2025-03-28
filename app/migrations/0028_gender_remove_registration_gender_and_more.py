# Generated by Django 5.1.5 on 2025-03-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_registration_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropdown_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='registration',
            name='gender',
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.ManyToManyField(to='app.gender'),
        ),
    ]
