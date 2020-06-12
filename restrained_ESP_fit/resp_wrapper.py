#!/usr/bin/env python3

import datetime
import os
import sys
import subprocess

def main():
    resp_binary = os.path.join(sys.prefix, 'resp')
    subprocess.run([resp_binary, *sys.argv[1:]]).check_returncode()
