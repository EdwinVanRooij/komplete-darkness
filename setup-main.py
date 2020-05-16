import os
import cx_Freeze
from cx_Freeze import setup, Executable

# ============================================================================================================
# === KompleteDarkness program
# ============================================================================================================
buildOptions = dict(
    includes=[
        "hid",
    ]
)
setup(
    name="KompleteDarkness",
    version="1.0.0",
    options=dict(build_exe=buildOptions),
    executables=[Executable(script="main/main.py", targetName="KompleteDarkness")]
)

# Manually add the icon
exe_path = os.path.abspath("build/exe.win32-3.7/KompleteDarkness.exe")
icon_path = os.path.abspath("icon/icon-komplete-darkness.ico")
cx_Freeze.util.AddIcon(exe_path, icon_path)
