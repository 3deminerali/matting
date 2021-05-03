import subprocess
import sys
import os
# path to python.exe
python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
# upgrade pip
subprocess.call([python_exe, "-m", "ensurepip"])
subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
# install required packages
subprocess.call([python_exe, "-m", "pip", "uninstall", "nummpy"])
subprocess.call([python_exe, "-m", "pip", "install", "numpy==1.17.0"])
subprocess.call([python_exe, "-m", "pip", "install", "-U", "pypiwin32"])
#subprocess.call([python_exe, "-m", "pip", "install", "mxnet"])
subprocess.call([python_exe, "-m", "pip", "install", "torch"])
subprocess.call([python_exe, "-m", "pip", "install", "torchvision"])
#subprocess.call([python_exe, "-m", "pip", "install", "gluoncv==0.8"])
subprocess.call([python_exe, "-m", "pip", "install", "matplotlib"])
#Maybe additionally install PIL or Pillow library if it is not already installed