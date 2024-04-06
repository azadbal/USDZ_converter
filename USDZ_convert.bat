@echo off

:: Change this directory to match your Blender 4.0+ install location
set BLENDER_PATH="C:\Program Files\Blender Foundation\Blender 4.0\blender.exe"  

:: Change this directory to match wherever you decide to place the python file 
set PYTHON_SCRIPT="X:\FILES\Code\BAT files\dependancies\scale_and_export.py"

:: Ensure that the directory path with spaces is correctly passed to the Python script
%BLENDER_PATH% --factory-startup --background --python %PYTHON_SCRIPT% -- %CD%
echo Process completed!
pause