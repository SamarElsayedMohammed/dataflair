# Generated by Django 3.1.3 on 2020-11-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
