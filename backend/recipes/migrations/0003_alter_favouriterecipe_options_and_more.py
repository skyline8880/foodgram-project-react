# Generated by Django 4.0.4 on 2022-06-10 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favouriterecipe',
            options={'ordering': ('-added_to_favorites', '-added_to_shopping_cart'), 'verbose_name': 'Favorites', 'verbose_name_plural': 'Favorites'},
        ),
        migrations.AlterModelOptions(
            name='ingredientamount',
            options={'ordering': ('id',), 'verbose_name': 'Ingredient amount', 'verbose_name_plural': 'Ingredient amounts'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('-created_date',), 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('id',), 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]