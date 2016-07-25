REM Please setup the path to pyrcc4.exe before executing this batch file.
REM The file should be found in <Your QGIS Install Directory>\bin\pyrcc4.exe
REM Ex. For Essen (verion 2.14.4),
REM C:\Program Files\QGIS Essen\bin\pyrcc4.exe
REM If using Essen, You can execute the pyrcc4_set_path.bat file from command prompt.

@ECHO OFF
REM Set the default plugin folder
SET PLUGIN_NAME=OpenAerialMap
SET OAM_PLUGIN_DIR=%HOMEPATH%\.qgis2\python\plugins\%PLUGIN_NAME%

ECHO Create OAM Plugin Directory %OAM_PLUGIN_DIR%
mkdir %OAM_PLUGIN_DIR%

REM Create resources_rc.py, help, and translation files
pyrcc4 -o ../resources_rc.py ../resources.qrc

REM SET HELPFILES=help
REM SET LOCALS=, LRELEASE=, etc.


SET FOLDERS=ext_libs gui icon module temp i18n
FOR %%f IN (%FOLDERS%) DO (
  xcopy ..\%%f %OAM_PLUGIN_DIR%\%%f\ /E /Y
)

SET TARGET_FILES=__init__.py ABOUT INSTALL LICENSE metadata.txt oam_main.py^
                oam-qgis-plugin.conf.sample resources.qrc resources_rc.py
FOR %%f IN (%TARGET_FILES%) DO (
  copy ..\%%f %OAM_PLUGIN_DIR%\%%f
)
