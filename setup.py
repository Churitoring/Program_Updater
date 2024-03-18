#python setup.py build
#pyinstaller jsongen.py --icon=programupdater.ico --noconsole --onefile
from cx_Freeze import setup, Executable 

setup(
    executables=[Executable("programupdater.py", icon="programupdater.ico")]
)
