from csv import reader

from django.core.management.base import BaseCommand

from ingredients.models import Metrics, MeasurementUnit, Ingredient


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
                'ingredients/data/ingredients.csv', 'r',
                encoding='UTF-8'
        ) as ingredients:
            for row in reader(ingredients):
                if len(row) == 2:
                    if row[1] == 'г' or row[1] == 'кг':
                        MeasurementUnit.objects.get_or_create(
                            name=row[1], metric=Metrics.mass
                        )
                    elif row[1] == 'мл' or row[1] == 'л':
                        MeasurementUnit.objects.get_or_create(
                            name=row[1], metric=Metrics.volume
                        )
                    elif row[1] == 'шт.':
                        MeasurementUnit.objects.get_or_create(
                            name=row[1], metric=Metrics.quantity
                        )
                    elif row[1] == '%' or row[1] == 'процент':
                        MeasurementUnit.objects.get_or_create(
                            name=row[1], metric=Metrics.percent
                        )
                    else:
                        MeasurementUnit.objects.get_or_create(
                            name=row[1], metric=Metrics.miscellaneous
                        )
                    Ingredient.objects.get_or_create(
                        name=row[0], measurement_unit=MeasurementUnit.objects.get(name=row[1]),
                    )
