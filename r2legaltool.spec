# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['r2legaltool.py'],
    pathex=[],
    binaries=[],
    datas=[('app/images/logo.png', 'app/images'), ('app/resources/label1.pdf', 'app/resources'), ('app/resources/label2.pdf', 'app/resources')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='r2legaltool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
