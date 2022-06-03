# Generated by Django 4.0.4 on 2022-06-03 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        ('ingredients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.IngredientAmount', to='ingredients.ingredient', verbose_name='ingredients'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='recipes', to='recipes.tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='ingredientamount',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredient_amounts', to='ingredients.ingredient', verbose_name='ingredient'),
        ),
        migrations.AddField(
            model_name='ingredientamount',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_amounts', to='recipes.recipe', verbose_name='recipe'),
        ),
        migrations.AddField(
            model_name='favouriterecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_favourites', to='recipes.recipe', verbose_name='recipe'),
        ),
        migrations.AddField(
            model_name='favouriterecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_recipes', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('author', 'name'), name='unique_recipe_author'),
        ),
        migrations.AddConstraint(
            model_name='ingredientamount',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='unique_recipe_ingredient'),
        ),
        migrations.AddConstraint(
            model_name='favouriterecipe',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_favorite_recipe'),
        ),
    ]
