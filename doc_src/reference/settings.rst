========
Settings
========


DEFAULT_SETTINGS = {
    'AUTOCOMPLETE_FIELDS': {},
    'AUTOCOMBOBOX_FIELDS': {},
    'AUTOCOMPLETESELECT_FIELDS': {},
    'AUTOCOMBOBOXSELECT_FIELDS': {},
    'AUTOCOMPLETESELECTMULTI_FIELDS': {},
    'AUTOCOMBOBOXSELECTMULTI_FIELDS': {},
}


<FOO>_FIELDS
============

Each of the settings is a ``dict`` in the format:

.. code-block:: python

   {
       'app.model.field': 'path.to.lookup.Class',
   }
