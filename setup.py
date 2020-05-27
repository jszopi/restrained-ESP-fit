from setuptools import setup
import subprocess

subprocess.run(["make"]).check_returncode()
subprocess.run(["./restrained_ESP_fit"]).check_returncode()  # Always returns 0

config = {
    'name': 'restrained_ESP_fit',
    'version': '2.4.1',
    'description': 'Fitting partial charges to molecular Electrostatic Potential field',
    'author': 'Jan Szopinski',
    'author_email': 'jszopi@users.noreply.github.com',
    'url': 'https://github.com/jszopi/restrained_ESP_fit',
    'packages': [],
    'license': 'GPLv3',
    'scripts': ["restrained_ESP_fit"],
}

setup(**config)
