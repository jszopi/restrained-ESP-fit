#!/usr/bin/env python3

import datetime
import pkg_resources
import sys
import subprocess

def main():
    resp_binary = pkg_resources.resource_filename(__name__, "resp")
    with open(f"temp+{datetime.datetime.now()}", 'w') as fh:
        fh.write(f"\n{resp_binary}")
    subprocess.run([resp_binary, *sys.argv[1:]]).check_returncode()
