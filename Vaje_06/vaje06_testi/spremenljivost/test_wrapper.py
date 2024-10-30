import importlib
import sys

to_run = input()

try:
    a=importlib.import_module(to_run)
    exit(0)
except Exception as e:
    sys.stderr.write(type(e).__name__+": "+str(e)+'\n')
    exit(1)
