# Generated by Django 5.0.4 on 2024-05-01 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.faculty'),
        ),
    ]
