# Generated by Django 3.0.6 on 2020-05-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='no_of_emp',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
