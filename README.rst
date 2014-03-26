=======
TVDb
=======

TVDb is a django application for TV channels DB.

Quick start
-----------

1. Add "tvdb" to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = (
          ...
          'tvdb',
       )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^tvdb/', include('tvdb.urls')),
