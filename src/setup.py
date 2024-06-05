from setuptools import setup

APP = ['view.py']
APP_NAME = 'SmartCalc_v3.0_'
DATA_FILES = []
OPTIONS = {
    'iconfile': 'icon.icns',
    'packages': ['numpy', 'matplotlib', 'PyQt5']
}

setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
