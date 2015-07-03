## oam-qgis-plugin

QGIS plugin to access and upload data to OpenAerialMap

## Install instructions

The plugin is still in early development phase, but tests and feedbacks are always appreciated.
Use the following commands to install it in a unix system:

$ git clone https://github.com/hotosm/oam-qgis-plugin.git 

$ cd oam-qgis-plugin/OpenAerialMap/ 

$ make deploy

Then activate the plugin through QGIS menu (Plugins -> Manage and Install Plugins).
You should see the OAM icons in your manu at this point.

After any change in the code you can re-deploy the plugin by doing:

$ cd oam-qgis-plugin/OpenAerialMap/ 

$ make clean 

$ make deploy

You also need to restart QGIS to reload the new compiled code.

## Rquired features

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
