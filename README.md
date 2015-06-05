## oam-qgis-plugin

QGIS plugin to access and upload data to OpenAerialMap

## Features

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

Weekly meetings on Wednesdays at 19h30 UTC on out gitter channel:
[![Join the chat at https://gitter.im/hotosm/oam-qgis-plugin](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hotosm/oam-qgis-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
