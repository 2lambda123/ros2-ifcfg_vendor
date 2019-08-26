from distutils.sysconfig import get_python_lib
import os
import subprocess
import sys


pre = sys.argv[1]
os.makedirs(get_python_lib(prefix=pre))
os.environ['PYTHONPATH'] = get_python_lib(prefix=pre)
process = subprocess.call([sys.executable, 'setup.py', 'install', '--prefix='+pre])
sys.stderr.write(repr(pre))
