import os
import cx_Freeze
from cx_Freeze import setup, Executable

# ============================================================================================================
# === Setup program
# ============================================================================================================
buildOptions = dict(
    includes=[
        "hid",
    ]
)
setup(
    name="KompleteDarknessSetup",
    version="1.0.0",
    options=dict(build_exe=buildOptions),
    executables=[Executable(script="main/setup.py", targetName="KompleteDarknessSetup")],
)

# Manually add the icon
exe_path_setup = os.path.abspath("build/exe.win32-3.7/KompleteDarknessSetup.exe")
icon_path_setup = os.path.abspath("icon/icon-komplete-darkness-setup.ico")
cx_Freeze.util.AddIcon(exe_path_setup, icon_path_setup)
