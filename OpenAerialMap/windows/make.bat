@ECHO OFF
REM Please setup the path to pyrcc4.exe before executing this batch file.
REM The file should be found in <Your QGIS Install Directory>\bin\pyrcc4.exe
REM Ex. For Essen (version 2.14.4),
REM SET PATH=%PATH%;C:\Program Files\QGIS Essen\bin or C:\Program Files\QGIS 2.14.4\bin, etc.


REM Set the default plugin folder
SET PLUGIN_NAME=OpenAerialMap
SET OAM_PLUGIN_DIR=%HOMEPATH%\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\%PLUGIN_NAME%

SET FOLDERS=ext_libs gui icon module temp i18n
SET TARGET_FILES=__init__.py ABOUT INSTALL LICENSE metadata.txt oam_main.py^
                oam-qgis-plugin.conf.sample resources.qrc set_env.py^
                resources_rc.py

REM Set the build folder for help files
SET HELP=help\build\html

REM set the resource folder for translation
REM SET LOCALS=, LRELEASE=, etc.

if "%1" == "deploy" (
  ECHO Create resources_rc.py
  pyrcc5 -o ..\resources_rc.py ..\resources.qrc

  ECHO Create OAM Plugin Directory %OAM_PLUGIN_DIR%
  mkdir %OAM_PLUGIN_DIR%

  FOR %%f IN (%FOLDERS%) DO (
    xcopy ..\%%f %OAM_PLUGIN_DIR%\%%f\ /E /Y
  )

  REM xcopy ..\%HELP% %OAM_PLUGIN_DIR%\help\ /E /Y

  FOR %%f IN (%TARGET_FILES%) DO (
    copy ..\%%f %OAM_PLUGIN_DIR%\%%f
  )

  ECHO Delete resources_rc.py file
  del ..\resources_rc.py
)
if "%1" == "derase" (
	ECHO under construction - derase
)
if "%1" == "doc" (
	ECHO Building help file in html format...
  REM CALL ..\help\make.bat html
)
if "%1" == "docclean" (
	ECHO Deleting help file...
  REM del ..\help\build /S /F /Q
)
