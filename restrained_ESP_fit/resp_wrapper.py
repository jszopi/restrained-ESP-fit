#!/usr/bin/env python3

import datetime
import pkg_resources
import sys
import subprocess

def main():
    resp_binary = pkg_resources.resource_filename(__name__, "build/resp")
    subprocess.run([resp_binary, *sys.argv[1:]]).check_returncode()
