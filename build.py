#!/usr/bin/env python

import os
from pathlib import Path
from plumbum import local, FG

cwd = Path.cwd()

for build_py in cwd.glob("*/**/build.py"):
    dir = build_py.parent
    print(build_py)
    try:
        os.chdir(dir)
        local["./build.py"] & FG
    finally:
        os.chdir(cwd)


