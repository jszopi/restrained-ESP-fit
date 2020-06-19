from setuptools import setup, Distribution
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

subprocess.run(["make"]).check_returncode()

config = {
    'name': 'restrained_ESP_fit',
    'version': '2.4.10',
    'description': 'Fitting partial charges to molecular Electrostatic Potential field',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'maintainer': 'Jan Szopinski',
    'maintainer_email': 'jszopi@users.noreply.github.com',
    'url': 'https://github.com/jszopi/restrained_ESP_fit',
    'license': 'GPLv3',
    'packages': ["restrained_ESP_fit"],
    'data_files': [(".", ["resp"])],
    'entry_points': {
        'console_scripts': ["restrained_ESP_fit=restrained_ESP_fit.resp_wrapper:main"],
    },
}

setup(**config)
