# Generated by Django 2.2.3 on 2019-07-11 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_auto_20190711_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmenttype',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.Course'),
        ),
    ]
