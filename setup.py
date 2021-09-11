from setuptools import setup
from setuptools import find_packages
import py2exe
setup(
    name="random_rom",
    version="0.1",
    install_requires=[],
    setup_requires=["wheel"],
    scripts=["random_rom.py"],
    entry_points={
        "console_scripts": [
            "random_rom.py=random_rom.py:main",
        ],
    },
    options={
        "py2exe": {
            "compressed": False,
            "unbuffered": True,
            "xref": True,
            "optimize": 2,
            "bundle_files": 1,
        },
    },
    console=["random_rom.py"],
)