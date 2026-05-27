# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_all

# Collect everything PySide6 needs
pyside6_datas, pyside6_binaries, pyside6_hidden = collect_all('PySide6')

# Collect librosa's data files (it needs its own internal data)
librosa_datas = collect_data_files('librosa')

# Collect numba data (librosa depends on it)
numba_datas = collect_data_files('numba')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=pyside6_binaries,
    datas=pyside6_datas + librosa_datas + numba_datas,
    hiddenimports=pyside6_hidden + [
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtMultimedia',
        'librosa',
        'librosa.core',
        'librosa.feature',
        'librosa.util',
        'soundfile',
        'audioread',
        'mido',
        'pyaudio',
        'pydub',
        'scipy.signal',
        'scipy.fft',
        'numba',
        'sklearn',
        'sklearn.utils._cython_blas',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'PyQt5',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
        'PyQt5.QtMultimedia',
        'PyQt6',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
        'PyQt6.QtMultimedia',
        'tkinter',
        '_tkinter',
        'matplotlib',  # remove this line if your app uses matplotlib
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='harmonize',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # False = no terminal window, GUI only
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name='harmonize.app',
    icon=None,              # replace None with 'assets/icon.icns' if you have one
    bundle_identifier='com.sreyasaju.harmonize',
)
