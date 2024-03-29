# Generated by Django 4.0.4 on 2022-06-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
                'ordering': ['name', 'measurement_unit'],
            },
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('metric', models.CharField(choices=[('mass', 'mass'), ('volume', 'volume'), ('quantity', 'quantity'), ('percent', 'percent'), ('miscellaneous', 'miscellaneous')], max_length=255, verbose_name='metric')),
            ],
            options={
                'verbose_name': 'Measurement unit',
                'verbose_name_plural': 'Measurement units',
                'ordering': ['metric', 'name'],
            },
        ),
        migrations.AddConstraint(
            model_name='measurementunit',
            constraint=models.UniqueConstraint(fields=('name', 'metric'), name='unique_measurement_metric'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='ingredients.measurementunit', verbose_name='measurement unit'),
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(fields=('name', 'measurement_unit'), name='unique_ingredient_unit'),
        ),
    ]
