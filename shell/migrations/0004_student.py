# Generated by Django 2.0.3 on 2018-04-03 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_cgpa',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)], verbose_name='current CGPA'),
        ),
    ]
