# Generated by Django 4.0.4 on 2022-07-09 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_alter_ingredient_measurement_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='ingredients.measurementunit', verbose_name='measurement unit'),
        ),
    ]
