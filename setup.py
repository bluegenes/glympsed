from setuptools import setup, find_packages
import glob
import os

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]

# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.

from glympsed import __version__, _program

CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: C++",
    "Programming Language :: Python :: 2.7",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
    name = _program,
    version = __version__,
    test_suite='pytest.collector',
    tests_require=['pytest'],
    python_requires='<3',
    description="",
    url="https://github.com/glympsed/glympsed",
    #packages = find_packages(), # doesn't work in 2.7
    #package_dir = {'': 'glympsed'},
    #pkgs not really working rn, copied relevant py files into glympsed dir
    packages = ['glympsed', 'glympsed.create-sim-data', 'glympsed.sample-models', 'glympsed.model-validity'],
    classifiers = CLASSIFIERS,
    entry_points="""
    [console_scripts]
    {program} = {program}.__main__:main
      """.format(program = _program),
    install_requires = required,
    include_package_data=True,
    package_data = { "glympsed": ["*/*.txt", "*/*.csv"
    ] },
    zip_safe=False
)
