# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all, collect_data_files

block_cipher = None

# --- PySide6 ---
pyside6_datas, pyside6_binaries, pyside6_hidden = collect_all("PySide6")

pyside6_hidden = [
    x for x in pyside6_hidden
    if "WebEngine" not in x
]

pyside6_binaries = [
    b for b in pyside6_binaries
    if "WebEngine" not in b[0]
]

# --- audio libs ---
librosa_datas = collect_data_files("librosa")
numba_datas = collect_data_files("numba")
scipy_datas = collect_data_files("scipy")

a = Analysis(
    ["main.py"],

    pathex=["."],

    binaries=pyside6_binaries,

    datas=pyside6_datas + librosa_datas + numba_datas + scipy_datas + [
        ("assets", "assets"),
        ("ui", "ui"),
        ("lily.wav", "."),
        ("sample_pitches.txt", "."),
        ("res_rc.py", "."),
    ],
    hiddenimports=pyside6_hidden + [
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "PySide6.QtMultimedia",

        "sounddevice",
        "soundfile",
        "mido",
        "numpy",
        "scipy",
        "librosa",
        "numba",
        "llvmlite",
        "sklearn",
        "joblib",
        "cffi",
        "pydub",
    ],

    excludes=[
        "PyQt5",
        "PyQt6",
        "tkinter",
        "_tkinter",
    ],
    runtime_hooks=["rthooks/qt_patch.py"],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="harmonize",
    debug=False,
    console=False,
)

app = BUNDLE(
    exe,
    name="harmonize.app",
    bundle_identifier="com.sreyasaju.harmonize",
)