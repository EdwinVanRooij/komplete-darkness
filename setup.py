import os
import cx_Freeze
from cx_Freeze import setup, Executable

executables = [
    Executable(
        script="main/main.py",
        targetName="Pianue"
    )
]

buildOptions = dict(
    includes=[
        "mido.backends.rtmidi",
    ],
    include_files=[
        "main/example-settings.json",
        "main/example-song.json",
        "main/example-practice-song.json",
    ]
)

setup(
    name="Pianue",
    version="1.0.3",
    description="Pianue lights up your creativity!",
    options=dict(build_exe=buildOptions),
    executables=executables
)

# Manually add the icon
exe_path = os.path.abspath("build/exe.win32-3.7/Pianue.exe")
icon_path = os.path.abspath("icon/icon.ico")
cx_Freeze.util.AddIcon(exe_path, icon_path)
