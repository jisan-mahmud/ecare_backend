# Generated by Django 5.0.4 on 2024-05-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_doctor_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='available_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='available_time',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
