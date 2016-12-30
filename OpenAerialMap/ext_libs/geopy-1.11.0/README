geopy
=====

|Build Status|

geopy is a Python 2 and 3 client for several popular geocoding web
services.

geopy makes it easy for Python developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources.

geopy includes geocoder classes for the `OpenStreetMap
Nominatim <https://wiki.openstreetmap.org/wiki/Nominatim>`__, `ESRI
ArcGIS <http://resources.arcgis.com/en/help/arcgis-rest-api/>`__,
`Google Geocoding API
(V3) <https://developers.google.com/maps/documentation/geocoding/>`__,
`Baidu
Maps <http://developer.baidu.com/map/webservice-geocoding.htm>`__, `Bing
Maps API <http://www.microsoft.com/maps/developers/web.aspx>`__, `Yahoo!
PlaceFinder <https://developer.yahoo.com/boss/geo/docs/>`__,
`Yandex <http://api.yandex.com/maps/doc/intro/concepts/intro.xml>`__,
`IGN
France <http://api.ign.fr/tech-docs-js/fr/developpeur/search.html>`__,
`GeoNames <http://www.geonames.org/>`__,
`NaviData <http://navidata.pl>`__,
`OpenMapQuest <http://developer.mapquest.com/web/products/open/geocoding-service>`__,
`What3Words <http://what3words.com/api/reference>`__,
`OpenCage <http://geocoder.opencagedata.com/api.html>`__,
`SmartyStreets <https://smartystreets.com/products/liveaddress-api>`__,
`geocoder.us <http://geocoder.us/>`__, and
`GeocodeFarm <https://www.geocodefarm.com/>`__ geocoder services. The
various geocoder classes are located in
`geopy.geocoders <https://github.com/geopy/geopy/tree/master/geopy/geocoders>`__.

geopy is tested against CPython 2.7, CPython 3.2, CPython 3.4, PyPy, and
PyPy3.

© geopy contributors 2006-2015 (see AUTHORS) under the `MIT
License <https://github.com/geopy/geopy/blob/master/LICENSE>`__.

Installation
------------

Install using `pip <http://www.pip-installer.org/en/latest/>`__ with:

::

    pip install geopy

Or, `download a wheel or source archive from
PyPI <https://pypi.python.org/pypi/geopy>`__.

Geocoding
---------

To geolocate a query to an address and coordinates:

::

    >>> from geopy.geocoders import Nominatim
    >>> geolocator = Nominatim()
    >>> location = geolocator.geocode("175 5th Avenue NYC")
    >>> print(location.address)
    Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
    >>> print((location.latitude, location.longitude))
    (40.7410861, -73.9896297241625)
    >>> print(location.raw)
    {'place_id': '9167009604', 'type': 'attraction', ...}

To find the address corresponding to a set of coordinates:

::

    >>> from geopy.geocoders import Nominatim
    >>> geolocator = Nominatim()
    >>> location = geolocator.reverse("52.509669, 13.376294")
    >>> print(location.address)
    Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
    >>> print((location.latitude, location.longitude))
    (52.5094982, 13.3765983)
    >>> print(location.raw)
    {'place_id': '654513', 'osm_type': 'node', ...}

Measuring Distance
------------------

Geopy can calculate geodesic distance between two points using the
`Vincenty
distance <https://en.wikipedia.org/wiki/Vincenty's_formulae>`__ or
`great-circle
distance <https://en.wikipedia.org/wiki/Great-circle_distance>`__
formulas, with a default of Vincenty available as the class
``geopy.distance.distance``, and the computed distance available as
attributes (e.g., ``miles``, ``meters``, etc.).

Here's an example usage of Vincenty distance:

::

    >>> from geopy.distance import vincenty
    >>> newport_ri = (41.49008, -71.312796)
    >>> cleveland_oh = (41.499498, -81.695391)
    >>> print(vincenty(newport_ri, cleveland_oh).miles)
    538.3904451566326

Using great-circle distance:

::

    >>> from geopy.distance import great_circle
    >>> newport_ri = (41.49008, -71.312796)
    >>> cleveland_oh = (41.499498, -81.695391)
    >>> print(great_circle(newport_ri, cleveland_oh).miles)
    537.1485284062816

Documentation
-------------

More documentation and examples can be found at `Read the
Docs <http://geopy.readthedocs.org/en/latest/>`__.

.. |Build Status| image:: https://travis-ci.org/geopy/geopy.svg?branch=master
   :target: https://travis-ci.org/geopy/geopy
