# Generated by Django 2.2.3 on 2019-07-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_auto_20190711_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='hours_spent',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
