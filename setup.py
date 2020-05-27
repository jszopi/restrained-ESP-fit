try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import subprocess

subprocess.run("make").check_returncode()
subprocess.run("./restrained_ESP_fit").check_returncode()

config = {
    'name': 'restrained_ESP_fit',
    'version': '2.4.1',
    'description': 'Fitting partial charges to molecular Electrostatic Potential field',
    'author': 'Jan Szopinski',
    'author_email': 'jszopi@users.noreply.github.com',
    'url': 'https://github.com/jszopi/restrained_ESP_fit',
    'packages': [],
    'license': 'GPLv3',
    'entry_points': {
        'console_scripts': ["restrained_ESP_fit=restrained_ESP_fit:main"]
    },
}

setup(**config)
