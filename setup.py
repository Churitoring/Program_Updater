#python setup.py build
from cx_Freeze import setup, Executable 

setup(
    name="Program Updater",
    version="0.0.2",
    description="Program Updater By Churitoring",
    executables=[Executable("programupdater.py", icon="programupdater.ico")]
)
