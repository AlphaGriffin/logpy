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


def fatal(_msg=None, *argv, **kwargs):
    """Log a fatal message.

    Fatal messages should be reserved for the most critical errors.
    These are generally halting errors.

    :param  _msg:   Message to log
    :type   _msg:   str
    """

    if this.level >= 1:
        _trace = 0
        if _msg is None:
            _trace = 2

        _log('!', 'F', _msg, _trace=_trace, *argv, **kwargs);


def error(_msg=None, *argv, **kwargs):
    """Log an error.

    Errors indicate a problem but are usually recoverable by the application.

    :param  _msg:   Message to log
    :type   _msg:   str
    """

    if this.level >= 2:
        _trace = 0
        if _msg is None:
            _trace = 2

        _log('%', 'E', _msg, _trace=_trace, *argv, **kwargs);


def warn(_msg=None, *argv, **kwargs):
    """Log a warning.

    Warnings indicate to the user a minor error state or possible condition that might require attention.

    :param  _msg:   Message to log
    :type   _msg:   str
    """

    if this.level >= 3:
        _trace = 0
        if _msg is None:
            _trace = 2

        _log('*', 'W', _msg, _trace=_trace, *argv, **kwargs);


def info(_msg, *argv, **kwargs):
    """Log something informative.

    An informational message helps the user follow what the program is doing.

    :param  _msg:   Message to log
    :type   _msg:   str
    """

    if this.level >= 4:
        _log('#', 'I', _msg, *argv, **kwargs);


def debug(_msg=None, *argv, **kwargs):
    """Log a message for debugging / diagnostic purposes.

    Debug messages are not intended for the casual user.

    :param  _msg:   Message to log
    :type   _msg:   str
    """

    if this.level >= 5:
        _trace = 0
        if _msg is None:
            _trace = 1

        _log('~', 'D', _msg, _trace=_trace, *argv, **kwargs);





def _log(_symbol, _letter, _msg, _trace=0, *argv, **kwargs):
    _msg = _handle(_symbol, _letter, _msg, False, _trace=_trace)

    for arg in argv:
        _handle(_symbol, _letter, arg, True, _trace=_trace)

    for name, value in kwargs.items():
        _handle(_symbol, _letter, value, True, _trace=_trace, _name=name)


def _handle(_symbol, _letter, _obj, _arg, _trace=0, _name=None):
    if isinstance(_obj, Exception):
        _msg = traceback.format_exc()
    elif _trace >= 2:
        #_msg = _obj[2].format_exc()
        _msg = traceback.format_exc()
    elif _trace >= 1:
        stack = inspect.stack()[3][0]
        locals = stack.f_locals
        lself = locals['self']
        if lself is not None:
            _msg = lself.__class__.__name__ + '::'
        else:
            _msg = ''
        code = stack.f_code
        _msg += code.co_name + str(code.co_varnames)
    else:
        _msg = str(_obj)

    lines = _msg.split('\n')
    for i, line in enumerate(lines):
        if i < 1:
            if not _arg:
                print(" {}{}{} {}".format(_symbol, _letter, _symbol, line))
            elif _name is None:
                print(" {} {} : => {}".format(_symbol, _symbol, line))
            else:
                print(" {} {} :{} => {}".format(_symbol, _symbol, _name, line))
        else:
            if not _arg:
                print(" {} {} {}".format(_symbol, _symbol, line))
            elif _name is None:
                print(" {} {} : => {}".format(_symbol, _symbol, line))
            else:
                print(" {} {} :{} => {}".format(_symbol, _symbol, _name, line))

