# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""Alpha Griffin Logging

A simple logging system for Python.

.. module:: ag.logging
   :platform: Unix
   :synopsis: Alpha Griffin Logging for Python
.. moduleauthor:: Shawn Wilson <lannocc@alphagriffin.com>
"""
from ag.logging.__version__ import __version__

import sys
this = sys.modules[__name__]
this.level = 0


NONE = 0
FATAL = 1
ERROR = 2
WARN = 3
INFO = 4
DEBUG = 5

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


def fatal(msg, *argv, **kwargs):
    """Log a fatal message.

    Fatal messages should be reserved for the most critical errors.
    These are generally halting errors.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 1:
        _log('!', 'F', msg, *argv, **kwargs);


def error(msg, *argv, **kwargs):
    """Log an error.

    Errors indicate a problem but are usually recoverable by the application.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 2:
        _log('%', 'E', msg, *argv, **kwargs);


def warn(msg, *argv, **kwargs):
    """Log a warning.

    Warnings indicate to the user a minor error state or possible condition that might require attention.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 3:
        _log('*', 'W', msg, *argv, **kwargs);


def info(msg, *argv, **kwargs):
    """Log something informative.

    An informational message helps the user follow what the program is doing.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 4:
        _log('#', 'I', msg, *argv, **kwargs);


def debug(msg, *argv, **kwargs):
    """Log a message for debugging / diagnostic purposes.

    Debug messages are not intended for the casual user.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 5:
        _log('~', 'D', msg, *argv, **kwargs);





def _log(symbol, letter, msg, *argv, **kwargs):
    lines = msg.split('\n')

    for i, line in enumerate(lines):
        if i < 1:
            print(" {}{}{} {}".format(symbol, letter, symbol, line))
        else:
            print(" {} {} {}".format(symbol, symbol, line))

    for arg in argv:
        print(" {} {} : => {}".format(symbol, symbol, arg))

    for name, value in kwargs.items():
        print(" {} {} :{} => {}".format(symbol, symbol, name, value))
