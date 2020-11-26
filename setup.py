"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='gamePyd',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',
    description='Read or emulate gamepads conviniently',
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8; variant=GFM',

    # The project's main homepage.
    url='https://github.com/PCPLays/gamePyd',

    # Author details
    author='Ayush Rawat (@PCplays)',
    author_email='rawatayush1997@gmail.com',

    # Choose your license
    license='Unlicense',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    keywords='virtual xbox controller xinput pyxinput',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # installs the DLL with the package
    package_data={
        'gamepyd': [
            'vXboxInterface-x64/vXboxInterface.dll',
            'vXboxInterface-x64/msvcp120.dll',
            'vXboxInterface-x64/msvcr120.dll',
            'vXboxInterface-x86/vXboxInterface.dll',
            'vXboxInterface-x86/msvcp120.dll',
            'vXboxInterface-x86/msvcr120.dll'
        ]
    })
