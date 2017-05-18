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
this.level = -1

import traceback
import inspect

NONE = 0
FATAL = 1
ERROR = 2
WARN = 3
INFO = 4
DEBUG = 5

def set(level):
    """Set log level.
    
    Sets the global cutoff level for logging output.
    This should be called early and need only be called once,
    as the cutoff gets fixed the first time this is called.
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
    if this.level == -1:
        this.level = level
    else:
        debug("ignoring subsequent call to log.set with:", level=level)


def fatal(msg=None, *argv, **kwargs):
    """Log a fatal message.

    Fatal messages should be reserved for the most critical errors.
    These are generally halting errors.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 1:
        trace = 0
        if msg is None:
            trace = 2

        _log('!', 'F', msg, trace=trace, *argv, **kwargs);


def error(msg=None, *argv, **kwargs):
    """Log an error.

    Errors indicate a problem but are usually recoverable by the application.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 2:
        trace = 0
        if msg is None:
            trace = 2

        _log('%', 'E', msg, trace=trace, *argv, **kwargs);


def warn(msg=None, *argv, **kwargs):
    """Log a warning.

    Warnings indicate to the user a minor error state or possible condition that might require attention.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 3:
        trace = 0
        if msg is None:
            trace = 2

        _log('*', 'W', msg, trace=trace, *argv, **kwargs);


def info(msg, *argv, **kwargs):
    """Log something informative.

    An informational message helps the user follow what the program is doing.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 4:
        _log('#', 'I', msg, *argv, **kwargs);


def debug(msg=None, *argv, **kwargs):
    """Log a message for debugging / diagnostic purposes.

    Debug messages are not intended for the casual user.

    :param  msg:    Message to log
    :type   msg:    str
    """

    if this.level >= 5:
        trace = 0
        if msg is None:
            trace = 1

        _log('~', 'D', msg, trace=trace, *argv, **kwargs);





def _log(symbol, letter, msg, trace=0, *argv, **kwargs):
    msg = _handle(symbol, letter, msg, False, trace=trace)

    for arg in argv:
        _handle(symbol, letter, arg, True, trace=trace)

    for name, value in kwargs.items():
        _handle(symbol, letter, value, True, trace=trace, name=name)


def _handle(symbol, letter, obj, arg, trace=0, name=None):
    if isinstance(obj, Exception):
        msg = traceback.format_exc()
    elif trace >= 2:
        #msg = obj[2].format_exc()
        msg = traceback.format_exc()
    elif trace >= 1:
        stack = inspect.stack()[3][0]
        locals = stack.f_locals
        lself = locals['self']
        if lself is not None:
            msg = lself.__class__.__name__ + '::'
        else:
            msg = ''
        code = stack.f_code
        msg += code.co_name + str(code.co_varnames)
    else:
        msg = str(obj)

    lines = msg.split('\n')
    for i, line in enumerate(lines):
        if i < 1:
            if not arg:
                print(" {}{}{} {}".format(symbol, letter, symbol, line))
            elif name is None:
                print(" {} {} : => {}".format(symbol, symbol, line))
            else:
                print(" {} {} :{} => {}".format(symbol, symbol, name, line))
        else:
            if not arg:
                print(" {} {} {}".format(symbol, symbol, line))
            elif name is None:
                print(" {} {} : => {}".format(symbol, symbol, line))
            else:
                print(" {} {} :{} => {}".format(symbol, symbol, name, line))

