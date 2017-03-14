# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
Alpha Griffin Logging

@author lannocc
"""
from ag.logging.__version__ import __version__

import sys
this = sys.modules[__name__]
this.level = 0

def set(level):
    """set log level"""
    this.level = level



def fatal(msg):
    if this.level >= 1:
        print(" #F# {}".format(msg))

def error(msg):
    if this.level >= 2:
        print(" %E% {}".format(msg))

def warn(msg):
    if this.level >= 3:
        print(" !W! {}".format(msg))

def info(msg):
    if this.level >= 4:
        print(" *I* {}".format(msg))

def debug(msg):
    if this.level >= 5:
        print(" ~D~ {}".format(msg))


