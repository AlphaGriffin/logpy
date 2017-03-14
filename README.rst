
===========================
Alpha Griffin Python Logger
===========================

Logging system for Python.

.. contents:: Table of Contents
.. toctree::
   API Documentation <api/modules>

These common log levels are defined:

1. **FATAL** - logic violation, major flaw, or potentially halting error
2. **ERROR** - these generally indicate a problem
3. **WARN** - warnings but not necessarily a problem
4. **INFO** - informational messages
5. **DEBUG** - verbose and often extraneous, but useful for debugging purposes


Install
-------

To install this project to the local system: ``python setup.py install``


Usage
-----

You can control the logging level with one of the 5 numerical levels defined above. A value of ``None`` or ``0`` will disable logging. Use one of the 5 log print functions (``debug()``, ``info()``, ``warn()``, ``error()``, ``fatal()``) in places where you might otherwise have used ``print()``.

Example usage of the logging system in a Python script::

    import ag.logging as log

    # set global logging level
    log.set(3) # see all WARN, ERROR, FATAL

    # some log printing examples
    log.warn('this warning message is shown at level 3')
    log.debug('this debug message is NOT shown at level 3')


Distributing
------------

Since we use the standard setuptools package, it is very easy to make source and binary distributions.

To make a *source* distribution::

    python setup.py sdist

To make a *binary* distribution::

    python setup.py bdist_wheel

The distributions will collect in the dist/ directory.

