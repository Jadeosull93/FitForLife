# Generated by Django 3.1.1 on 2020-10-19 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
        ('planworkouts', '0002_auto_20201019_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='planworkout',
            name='workout_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.workout'),
        ),
    ]
