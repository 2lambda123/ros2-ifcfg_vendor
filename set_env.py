from distutils.sysconfig import get_python_lib
import os
from pathlib import Path
import subprocess
import sys


pre = sys.argv[1]
os.makedirs(Path(get_python_lib(prefix=pre)))
os.environ['PYTHONPATH'] = Path(get_python_lib(prefix=pre))
process = subprocess.call([sys.executable, 'setup.py', 'install', '--prefix='+pre])
sys.stderr.write(repr(pre))
