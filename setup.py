#python setup.py build
#pyinstaller programupdater.py --icon=programupdater.ico
from cx_Freeze import setup, Executable 

setup(
    name="Program Updater",
    version="1.0.4",
    description="Program Updater By Churitoring",
    executables=[Executable("programupdater.py", icon="programupdater.ico")]
)
