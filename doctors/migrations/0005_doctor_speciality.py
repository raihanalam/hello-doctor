# Generated by Django 5.0.4 on 2024-05-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_remove_doctor_degree_alter_doctor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
