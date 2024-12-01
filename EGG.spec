# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect data files for matplotlib, pandas, and other libraries
matplotlib_data = collect_data_files('matplotlib', subdir='mpl-data')
pandas_data = collect_data_files('pandas')
numpy_data = collect_data_files('numpy')
sympy_data = collect_data_files('sympy')

# Collect submodules for all major libraries
matplotlib_submodules = collect_submodules('matplotlib')
pandas_submodules = collect_submodules('pandas')
numpy_submodules = collect_submodules('numpy')
sympy_submodules = collect_submodules('sympy')

# Combine all necessary data and submodules
all_datas = matplotlib_data + pandas_data + numpy_data + sympy_data + [
    ('EGG.ico', '.'),        # Include the icon file for the executable
    ('EGG.png', '.'),        # Include the image file for the executable
]

hidden_imports = matplotlib_submodules + pandas_submodules + numpy_submodules + sympy_submodules + [
    'tkinter',              # Tkinter for GUI
    'PIL',                  # Python Imaging Library (Pillow)
    'csv',                  # CSV module
]

# Define the Analysis step
a = Analysis(
    ['EGG.py'],
    pathex=['C:\\Users\\thunt\\OneDrive\\Documents\\EGG-Easy-Graph-Generator'],
    binaries=[],
    datas=all_datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# Package the Python files into a .pyz archive
pyz = PYZ(a.pure)

# Define the EXE step to create the executable
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='EGG',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True if you want a console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='EGG.png',  # Set the executable icon
)
