ECHO off

SETLOCAL enabledelayedexpansion

ECHO Setting up a clean directory: _Virtual

::ECHO     Does _Virtual directory exists?
::CD _Virtual
::IF !ERRORLEVEL! GTR 0 (
::    ECHO     Directory doesn't exist, creating...
::    MD _Virtual
::    GOTO make_dir
::) ELSE (
::    ECHO     Directory exists, erasing files...
::    ::DEL /F /Q *.*
::    RD /S /Q
::)
::CD ..
::ECHO     Finished

:del_dir
ECHO Does _Virtual exist?
CD _Virtual
IF NOT !ERRORLEVEL! GTR 0 (
    ECHO     Remove _Virtual
    CD ..
    RD /S /Q _Virtual
    GOTO del_dir
)

:make_dir
ECHO Create _Virtual ...
CD _Virtual
IF !ERRORLEVEL! GTR 0 (
    ECHO     Create _Virtual
    MD _Virtual
    GOTO make_dir
) ELSE (
    CD ..
)

ECHO 1. Installing a virtual python environment
ECHO 2. Activating virtual Python
ECHO 3. Updating pip
ECHO 4. Installing packs: setuptools, wheel
ECHO 5. Installing packs from requirements.txt
ECHO 6. List installed packs
::python -m venv _Virtual
::cmd /k "python -m venv _Virtual & Activate.bat & UpdatePip.bat & Install_FromRequirements.bat"
cmd /k "python -m venv _Virtual & Activate.bat & UpdatePip.bat & Install_BasicPacks.bat & Install_FromRequirements.bat & ListPacks.bat"


:done
SETLOCAL
EXIT /B
