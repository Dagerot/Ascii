:: remove old files
if exist Ascii.exe del Ascii.exe > NUL
if exist _py2exe rd /S /Q _py2exe

md _py2exe > NUL
copy Ascii.py _py2exe\Ascii.py

cd _py2exe
call pyinstaller -F Ascii.py

cd ..
copy _py2exe\dist\Ascii.exe Ascii.exe

:: clean up
if exist _py2exe rd /S /Q _py2exe
