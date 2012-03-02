from simpleapp.models import Fruit
from selectable.base import ModelLookup
from selectable.registry import registry

class FruitLookup(ModelLookup):
    model = Fruit
    search_fields = ('name__icontains', )
    
    def get_item_id(self, item):
        return item.id

registry.register(FruitLookup)