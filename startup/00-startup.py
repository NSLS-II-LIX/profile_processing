import logging,sys

#import ophyd
#ophyd.utils.startup.setup()

import bluesky
#from ophyd import *
#from ophyd.commands import *

def reload_macros(file='~/.ipython/profile_collection/startup/99-macros.py'):
    ipy = get_ipython()
    ipy.magic('run -i '+file)


def is_ipython():
    ip = True
    if 'ipykernel' in sys.modules:
        ip = False # Notebook
    elif 'IPython' in sys.modules:
        ip = True # Shell
    return ip
