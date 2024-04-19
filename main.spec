# -*- mode: python ; coding: utf-8 -*-

face_models = [
('./face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat', './face_recognition_models/models'),
('./face_recognition_models/models/mmod_human_face_detector.dat', './face_recognition_models/models'),
('./face_recognition_models/models/shape_predictor_5_face_landmarks.dat', './face_recognition_models/models'),
('./face_recognition_models/models/shape_predictor_68_face_landmarks.dat', './face_recognition_models/models'),
]
a = Analysis(
    [
        'main.py',
        'recognize.py',
        'faces_list.py',
        'camera_source.py',
        'change_window.py',
        'face_recognition_imp.py',
        'file_utils.py'
    ],
    pathex=[],
    binaries=face_models,
    datas=[],
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
    name='BossIsHere',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(exe,
         name='BossIsHere.app',
         icon=None,
         info_plist={
            'CFBundleName':'BossIsHere',
            'CFBundleDisplayName':'BossIsHere',
            'NSCameraUsageDescription':'Use your camera to find your boss',
            'NSAppleEventsUsageDescription':'Need to activate application which you appoint'
         },
         bundle_identifier='xyz.zxylovefq.boss_is_here')