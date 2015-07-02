This folder is still here for historical purposes, in case one wants to check the evolution of the plugin interface.

The current interface can be generated using the xml provided in the plugin repository ([oam_client_dialog_base.ui](https://raw.githubusercontent.com/hotosm/oam-qgis-plugin/master/OpenAerialMap/oam_client_dialog_base.ui)).

Execute the following commands in a terminal to generate and execute the python code:

> $ pyuic4 -xo oam_client_dialog_base.py oam_client_dialog_base.ui

> $ python oam_client_dialog_base.py 
