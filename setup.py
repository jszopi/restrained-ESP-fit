from setuptools import setup, Distribution
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

subprocess.run(["make"]).check_returncode()

class BinaryDistribution(Distribution):
    def has_ext_modules(_):  # I think this takes no arguments in Python 3.8
        return True


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
    'data_files': [(".", ["resp"])],
    'entry_points': {
        'console_scripts': ["restrained_ESP_fit=resp_wrapper:main"],
    },
    'distclass': BinaryDistribution
}

setup(**config)
