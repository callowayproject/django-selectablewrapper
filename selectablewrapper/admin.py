from django.contrib import admin

from .settings import REGISTRY, CSS, JS

class AutocompleteAdmin(admin.ModelAdmin):
    selectable_fields = {}
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.selectable_fields:
            widget = self.selectable_fields[db_field.name]['widget']
            lookup = self.selectable_fields[db_field.name]['lookup']
            return db_field.formfield(
                widget=widget(lookup))
        return super(AutocompleteAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    
    class Media:
        css = CSS
        js = JS


for model, modeladmin in admin.site._registry.items():
    if model in REGISTRY:
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (AutocompleteAdmin, modeladmin.__class__), {
            'selectable_fields': REGISTRY[model],
        }))