# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""Alpha Griffin Logging

A simple logging system for Python.

.. module:: ag.pyproject
   :platform: Unix
   :synopsis: Python Starter Project for Alpha Griffin
.. moduleauthor:: Shawn Wilson <lannocc@alphagriffin.com>
"""
from ag.logging.__version__ import __version__

import sys
this = sys.modules[__name__]
this.level = 0



def set(level):
    """Set log level.
    
    Sets the global cutoff level for logging output.
    This should be called early and should only be called once.
    If no level is set then the logging system is disabled.

    :param  level:  Log printing threshold
    :type   level:  int

    .. note::
        Use one of the following log levels:
            0. ``NONE``: all logging disabled
            1. ``FATAL``: fatal messages only
            2. ``ERROR``: errors and fatal messages
            3. ``WARN``: warnings, errors, and fatal messages
            4. ``INFO``: information, warnings, errors, and fatal messages
            5. ``DEBUG``: all logging enabled
    """
    this.level = level


def fatal(msg):
    """Log a fatal message.

    Fatal messages should be reserved for the most critical errors.
    These are generally halting errors.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 1:
        print(" #F# {}".format(msg))


def error(msg):
    """Log an error.

    Errors indicate a problem but are usually recoverable by the application.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 2:
        print(" %E% {}".format(msg))


def warn(msg):
    """Log a warning.

    Warnings indicate to the user a minor error state or possible condition that might require attention.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 3:
        print(" !W! {}".format(msg))


def info(msg):
    """Log something informative.

    An informational message helps the user follow what the program is doing.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 4:
        print(" *I* {}".format(msg))


def debug(msg):
    """Log a message for debugging / diagnostic purposes.

    Debug messages are not intended for the casual user.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 5:
        print(" ~D~ {}".format(msg))


