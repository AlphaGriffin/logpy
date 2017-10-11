
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

Installation Instructions
--------------

Install with pip directly from this repository.
  .. highlight:: bash
  :linenos:

  pip install git+https://github.com/alphagriffin/logpy

  Win10 x64: Working

Build Overview
--------------

Both a Makefile and setup.py are provided and used. The setup.py uses Python's standard setuptools package and you can call this script directly to do the basic Python tasks such as creating a wheel, etc.

The most common project build tasks are all provided in the Makefile. To see the full list of project targets::

    make help

Sphinx is used to generate html documentation and man pages. All documentation (html as well as man pages) may be regenerated at any time with::

    make docs

Every so often, when new source class files are created or moved, you will want to regenerate the API documentation templates. These templates may be modified by hand so this task does not overwrite existing files; you'll need to remove any existing files from ``api/`` that you want recreated. Then generate the API templates and re-build all documentation as follows::

    make apidoc
    make docs

There's not much to do for a simple Python project but your build may want to do more. In any case you can call ``make python`` if you need to (in pyproject this target simply delegates to ``./setup.py build``).

Build all the common tasks (including documentation) as follows::

    make all

To clean up all the common generated files from your project folder::

    make clean

To install this project to the local system::

    make install

Note that you may need superuser permissions to perform the above step.


Distributing
------------

To make a *binary* distribution::

    make bdist

(in pyproject, the above step simply delegates to ``./setup.py bdist_wheel``)

The distributions will collect in the ``dist/`` directory.


Using
-----

You can control the logging level with one of the 5 numerical levels defined above. A value of ``None`` or ``0`` will disable logging. Use one of the 5 log print functions (``debug()``, ``info()``, ``warn()``, ``error()``, ``fatal()``) in places where you might otherwise have used ``print()``.

Example usage of the logging system in a Python script::

    import ag.logging as log

    # set global logging level
    log.set(log.WARN) # see all WARN and higher (WARN, ERROR, FATAL)

    # some log printing examples
    log.warn('this warning message is shown at level 3')
    log.debug('this debug message is NOT shown at level 3')

If you have not installed the project system-wide or you have some changes to try, you must add the project folder to Python's search path first::

    import sys, os
    sys.path.insert(0, os.path.abspath('/path/to/logpy'))
    import ag.logging
