## oam-qgis-plugin

QGIS plugin to access and upload data to OpenAerialMap

## Install

An experimental package containing all the needed dependencies is available at http://acaia.ca/~tassia/OpenAerialMap-0.1alpha1.tar.gz

After performing the following steps you should see OAM icons in QGIS action bar:

* Unpack the file OpenAerialMap-0.1-alpha.1.tar.gz
* Place the resulting directory in QGIS plugins directory
* Activate the plugin through QGIS menu (Plugins -> Manage and Install Plugins)


## Build

Build, tests and feedbacks are super appreciated, specially in this early development phase.

The plugin depends on the following python libraries that are not installed by default with QGIS:

* [Boto](https://pypi.python.org/pypi/boto) - Amazon Web Services Library
* [FileChunkIO](https://pypi.python.org/pypi/filechunkio/) - represents a chunk of an OS-level file containing bytes data
* [python-pyproj](https://pypi.python.org/pypi/pyproj/) - Python interface to PROJ.4 library (>=1.9.4-1) 

If you have python-pip installed, all dependecies can be installed with the command:

$ pip install filechunkio boto pyproj

If you use UNIX, check first if your distribution provides corresponding packages. 

After installing dependencies you can proceed to get the plugin code and deploy:

$ git clone https://github.com/hotosm/oam-qgis-plugin.git 

$ cd oam-qgis-plugin/OpenAerialMap/ 

$ make deploy

Then activate the plugin through QGIS menu (Plugins -> Manage and Install Plugins). You should see the OAM icons in your manu at this point.

After any change in the code you should run 'make deploy' again. You also need to restart QGIS to reload the new compiled code. A handy alternative is to use the "Plugin Reloader" plugin to reload and live test your changes on the code. 

## Required features

* select input data (from individual files, a VRT or a loaded layer)
* insert/load/change metadata
* validate metadata
* choose OIN upload destination
* upload transaction
* notify OAM of new OIN resource
* trigger tile service on OAM
* authenticate to OAM (if requesting tile service)
* provide additional OAM metadata (if requesting tile service)
* re-projecting to EPSG:3857 (optional)
* convert format to GeoTIFF RGB (optional)

## Development guidelines

1. Use of qtcreator for:
  1. GUI layout/development
  2. defining most of the common signals/slots for the GUI components
2. Do not change any generated code directly but create a subclass and then
override/extend it, to keep our code and the automatically generated code
separated
3. Use QgisPluginCreator that has some basics setup (eg. internationalzation support)
4. Package any external python modules as part of the plugin

## Timeline

The development progress can be followed through the repository [Millestones](https://github.com/hotosm/oam-qgis-plugin/milestones).

## Communication channel

Weekly meetings on Wednesdays at 19h30 UTC on our gitter channel:

[![Join the chat at https://gitter.im/hotosm/oam-qgis-plugin](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hotosm/oam-qgis-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
