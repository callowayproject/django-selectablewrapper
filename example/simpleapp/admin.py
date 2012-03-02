from django.contrib import admin

from .models import Fruit, FavoriteFruit, FruitCombo

admin.site.register(Fruit)
admin.site.register(FavoriteFruit)
admin.site.register(FruitCombo)