from setuptools import setup
import distutils.command.build
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()


class build_(distutils.command.build.build):

    def run(self):
        print("Running build")
        subprocess.run(["make"]).check_returncode()
        subprocess.run(["mv", "resp", "restrained_ESP_fit"]).check_returncode()
        distutils.command.build.build.run(self)


config = {
    'name': 'restrained_ESP_fit',
    'description': 'Fitting partial charges to molecular Electrostatic Potential field',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'maintainer': 'Jan Szopinski',
    'maintainer_email': 'jszopi@users.noreply.github.com',
    'url': 'https://github.com/jszopi/restrained_ESP_fit',
    'license': 'GPLv3',
    'packages': ["restrained_ESP_fit"],
    'package_data': {"restrained_ESP_fit": ["resp"]},
    # Hacky? Causes the `resp` binary to be included in bdist_wheel but not in sdist
    'include_package_data': True,
    'entry_points': {
        'console_scripts': ["restrained_ESP_fit=restrained_ESP_fit.resp_wrapper:main"],
    },
    'cmdclass': {'build': build_},
    'use_scm_version': True,
    'setup_requires': ["setuptools_scm"],
    'python_requires': ">=3",
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    'keywords': ["restrained molecular electrostatic potential ESP fitting RESP charges"]
}

setup(**config)
