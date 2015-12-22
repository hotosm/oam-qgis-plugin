## oam-qgis-plugin

QGIS plugin to upload data to and access data from OpenAerialMap. The upload module and settings handling work, but the browser/catalog tab is still a non-functional module.

Contact sysadmin@hotosm.org to request an access key if you want to upload to the HOT OIN upload bucket.

## Install

A package containing all the needed dependencies is available at the [QGIS repository](https://plugins.qgis.org/plugins/OpenAerialMap/).

It can be installed through the QGIS menu "Plugins" -> "Manage and Install Plugins". Make sure that the option "Show also experimental plugins" is checked, at the Settings tab, otherwise the OAM plugin will not be shown among the available ones.

Alternatively, the plugin can be downloaded directly from the [repository](https://plugins.qgis.org/plugins/OpenAerialMap/version/0.1-alpha.2/download/), followed by:

* Unpacking the file OpenAerialMap-0.1-alpha.1.tar.gz
* Placing the resulting directory in QGIS plugins directory
* Activating the plugin through QGIS menu ("Plugins" -> "Manage and Install Plugins")

After activation of the plugin one should see the OAM icons at the QGIS action bar:

## Build

Builds, tests and feedbacks are very much appreciated by the development team. The plugin depends on the following python libraries that are not installed by default with QGIS:

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

Then activate the plugin through QGIS menu "Plugins" -> "Manage and Install Plugins". You should see OAM icons in your menu at this point.

After any change in the code you need to run 'make deploy' again. You also need to restart QGIS to reload the new compiled code. A handy alternative is to use the "Plugin Reloader" plugin to reload and live test your changes on the code. 

## Required features

During the plugin planning phase, those were the identified required features

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

The development progress can be followed through the repository [issues](https://github.com/hotosm/oam-qgis-plugin/issues) and [Millestones](https://github.com/hotosm/oam-qgis-plugin/milestones).

## Communication channel

Regular meetings are not being held at the moment, but please leave any comment or request on our gitter channel:

[![Join the chat at https://gitter.im/hotosm/oam-qgis-plugin](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hotosm/oam-qgis-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
