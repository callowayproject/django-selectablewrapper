from django.conf import settings
from django.db.models import get_model
from django.utils.importlib import import_module

from selectable.forms.widgets import (AutoCompleteWidget, AutoComboboxWidget, 
                        AutoCompleteSelectWidget, AutoComboboxSelectWidget, 
                        AutoCompleteSelectMultipleWidget, 
                        AutoComboboxSelectMultipleWidget )

DEFAULT_SETTINGS = {
    'AUTOCOMPLETE_FIELDS': {},
    'AUTOCOMBOBOX_FIELDS': {},
    'AUTOCOMPLETESELECT_FIELDS': {},
    'AUTOCOMBOBOXSELECT_FIELDS': {},
    'AUTOCOMPLETESELECTMULTI_FIELDS': {},
    'AUTOCOMBOBOXSELECTMULTI_FIELDS': {},
    'CSS': {'all': ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.13/themes/ui-lightness/jquery-ui.css',)},
    'JS': ('http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js',
           'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.13/jquery-ui.min.js',)
}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'SELECTABLEWRAPPER_SETTINGS'))

WIDGET_MAP = (
    ('AUTOCOMPLETE_FIELDS', AutoCompleteWidget),
    ('AUTOCOMBOBOX_FIELDS', AutoComboboxWidget),
    ('AUTOCOMPLETESELECT_FIELDS', AutoCompleteSelectWidget),
    ('AUTOCOMBOBOXSELECT_FIELDS', AutoComboboxSelectWidget),
    ('AUTOCOMPLETESELECTMULTI_FIELDS', AutoCompleteSelectMultipleWidget),
    ('AUTOCOMBOBOXSELECTMULTI_FIELDS', AutoComboboxSelectMultipleWidget),
)

REGISTRY = {}
# REGISTRY = {
#     ModelClass: {
#         'field': {'widget': widget, 'lookup': lookupclass, }
#     }
# }

for setting, widget in WIDGET_MAP:
    for field_string, lookup_class_string in USER_SETTINGS[setting].items():
        bits = field_string.split(".")
        model = get_model(bits[0], bits[1])
        field = bits[2]
        bits = lookup_class_string.split(".")
        lookup_class = getattr(import_module(".".join(bits[:-1])), bits[-1])
        REGISTRY.setdefault(model, {})[field] = {
            'widget': widget,
            'lookup': lookup_class
        }

globals().update(USER_SETTINGS)