import py2exe
from distutils.core import setup

options = {
    "bundle_files": 1,
    "compressed" : 1,
    "optimize" : 2,
}

setup(
    console = ["Mygame.py"],
    options = {"py2exe" : options},
    zipfile = None
)