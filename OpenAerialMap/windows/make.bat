@ECHO OFF
REM Please setup the path to pyrcc4.exe before executing this batch file.
REM The file should be found in <Your QGIS Install Directory>\bin\pyrcc4.exe
REM Ex. For Essen (version 2.14.4),
REM C:\Program Files\QGIS Essen\bin
REM If using Essen, You can execute the pyrcc4_set_path.bat file from command prompt.

REM Set the default plugin folder
SET PLUGIN_NAME=OpenAerialMap
SET OAM_PLUGIN_DIR=%HOMEPATH%\.qgis2\python\plugins\%PLUGIN_NAME%

SET FOLDERS=ext_libs gui icon module temp i18n
SET TARGET_FILES=__init__.py ABOUT INSTALL LICENSE metadata.txt oam_main.py^
                oam-qgis-plugin.conf.sample resources.qrc resources_rc.py

REM Create help, and translation files
REM SET HELPFILES=help
REM SET LOCALS=, LRELEASE=, etc.

ECHO Create resources_rc.py
pyrcc4 -o ../resources_rc.py ../resources.qrc

if "%1" == "deploy" (
  ECHO Create OAM Plugin Directory %OAM_PLUGIN_DIR%
  mkdir %OAM_PLUGIN_DIR%

  FOR %%f IN (%FOLDERS%) DO (
    xcopy ..\%%f %OAM_PLUGIN_DIR%\%%f\ /E /Y
  )

  FOR %%f IN (%TARGET_FILES%) DO (
    copy ..\%%f %OAM_PLUGIN_DIR%\%%f
  )
  
  ECHO Delete resources_rc.py file
  del ..\resources_rc.py
)
if "%1" == "derase" (
	echo under construction - derase
)
if "%1" == "doc" (
	echo under construction - doc
)
