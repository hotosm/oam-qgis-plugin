## oam-qgis-plugin

QGIS plugin to upload and download data to/from OpenAerialMap. The plugin cosists of following functionalities:  
1) Create, edit OIN conformed metadata from imagery and user input  
2) Upload imagery and metadata, using AWS-S3 bucket  
3) Search, browse, and download imagery and metadata through OAM catalog  
4) Support simple raster image processing, such as reprojection and file format conversion, as well as trigger the creation of tile service (currently under development)

Contact sysadmin@hotosm.org to request an access key if you want to upload to the HOT OIN upload bucket.

## Install from package

###### Use of plugin manager
A package containing all the needed dependencies can be installed through QGIS Plugin Manager. To install from plugin manager:  
1. Click the menu "Plugins" -> "Manage and Install Plugins".
2. Enter 'Open Aerial Map' in search box.  

Note: Make sure that "Show also experimental plugins" is checked at the Settings tab, otherwise the OAM plugin will not be shown among the available ones.

###### Download from plugin repository
Alternatively, you can directly download from  [repository](https://plugins.qgis.org/plugins/OpenAerialMap/).  
To install:
1. Unpack the dowloaded file 'OpenAerialMap-xxxx.zip'.  
2. Place the extracted files/folder in QGIS plugins directory.
3. Activate the plugin through QGIS menu ("Plugins" -> "Manage and Install Plugins").
4. You can see the OAM icons at the QGIS action bar, if plugin is activated.

## Build from source code

###### Dependencies:
* [Sphinx](http://www.sphinx-doc.org/en/stable/install.html) - To create help file, Sphinx documentation generator is being used in this plugin. To install Sphinx, please refer to the OS specific instructions at the website. (NOTE: As of July 2016, document generation is supported only in Linux environment. Threfore, users of other operating systems can ignore the dependency of Sphinx.)
* [Python](https://www.python.org/) - Installation of Sphinx requires python. If your operating system doesn't have python installed, please refer to the instruction at the website. Version 2.7 is presently being used for this plugin development.
* pyrcc4 - To compile Qt4 resource files into python code, pyrcc4 command must be used. Please refer to the OS specific instructions below for its installation or setting path.

###### Linux
1. Install pyrcc4:  
The easiest way to install pyrcc4 is probably to use package manager.
If using ubuntu 14.04 or its comatible distributions, following command should work:  
&nbsp;&nbsp;&nbsp;&nbsp;apt-get install pyqt4-dev-tools  
For the other distributions, please use the online resourece to get the information.

2. Download the repository and deploy the code to the plugin directory:  
$ git clone https://github.com/hotosm/oam-qgis-plugin.git  
$ cd oam-qgis-plugin/OpenAerialMap/  
$ make deploy

###### Windows
1. Set the path to pyrcc4.exe:  
To execute the make.bat file in MS-Windows, you need to set the path to pyrcc4.exe. Probably, the easiest way to set the path is to use OSGeo4W Shell. (If you open the shell, the path to the file should be automatically set.) However, you can also manually set the path from normal command prompt.

  1. Find the pyrcc4.exe file in the QGIS folder:  
  Ex. For the version 2.14.4 (Essen), C:\Program Files\QGIS 2.14.4\bin\ or C:\Program Files\QGIS Essen\bin\

  2. Set the path, using set command:  
  Ex. For the example above, execute SET PATH=%PATH%;C:\Program Files\QGIS 2.14.4\bin or C:\Program Files\QGIS Essen\bin

2. Download the repository and deploy the code to the plugin directory:  
$ git clone https://github.com/hotosm/oam-qgis-plugin.git  
$ cd oam-qgis-plugin\OpenAerialMap\windows\  
$ make.bat deploy

## Activate or reload deployed plugin

You can activate the deployed plugin through QGIS menu "Plugins" -> "Manage and Install Plugins". You should see OAM icons in your menu at this point.

After any change in the code you need to run 'make deploy' again. You also need to restart QGIS to reload the new compiled code. A handy alternative is to use the "Plugin Reloader" plugin to reload and live test your changes on the code. If necessary, you can also use 'make derase' command to erase the deployed folder completely.

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

1. Use of Qt4 Designer for:
  1. GUI layout/development
  2. defining most of the common signals/slots for the GUI components
2. Do not change any generated code directly but create a subclass and then
override/extend it, to keep our code and the automatically generated code
separated
3. Use QgisPluginCreator that has some basics setup (eg. internationalzation support)
4. Package any external python modules as a part of the plugin

## Timeline

The development progress can be followed through the repository [issues](https://github.com/hotosm/oam-qgis-plugin/issues) and [Millestones](https://github.com/hotosm/oam-qgis-plugin/milestones).

## Communication channel

Regular meetings are not being held at the moment, but please leave any comment or request on our gitter channel:

[![Join the chat at https://gitter.im/hotosm/oam-qgis-plugin](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hotosm/oam-qgis-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
