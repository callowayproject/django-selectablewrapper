===============
Getting Started
===============


#. Add selectablewrapper to INSTALLED_APPS

#. Create SELECTABLEWRAPPER_SETTINGS dictionary in settings.py

#. Create a FK_

{
   'AUTOCOMPLETE_FIELDS': {
      'app.model.field': 'autocomplete.class.path',
   },
   'AUTOCOMBOBOX_FIELDS': {
      'app.model.field': 'autocomplete.class.path',
   },
   'AUTOCOMPLETESELECT_FIELDS': {
      'app.model.field': 'autocomplete.class.path',
   },
   'AUTOCOMBOBOXSELECT_FIELDS': {
      'app.model.field': 'autocomplete.class.path',
   },
   'AUTOCOMPLETESELECTMULTI_FIELDS': {
      'app.model.field': 'autocomplete.class.path',
   },
   'AUTOCOMBOBOXSELECTMULTI_FIELDS': {
      'app.model.field': 'autocomplete.class.path',
   },
}

Modify the CSS and JS settings

Don't use AUTOCOMPLETE or AUTOCOMBOBOX for related fields! Use the select or selectmulti versions.

