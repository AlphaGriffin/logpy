#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""AlphaGriffin setuptools build script.

@author lannocc

@see    https://packaging.python.org/en/latest/distributing.html
@see    https://github.com/pypa/sampleproject

Some of this script logic also taken from:
        https://github.com/google/protobuf
"""

# FIXME / note to self:
#  read more at https://caremad.io/posts/2013/07/setup-vs-requirement/
#  -- to integrate fully pip



# -------------------------------------------------------------------------------------
#
# CUSTOMIZE THIS SECTION
#   All the variables defined here should be customized for your project.
#

NS      = 'ag'                          # namespace / meta-package folder
NAME    = 'logging'                     # should match source package name in NS folder
REQUIRE = ['sphinx_rtd_theme']          # package dependencies

DESC    = 'Alpha Griffin Python Logging'
TAGS    = 'logger utilities'            # space-separated list of keywords

AUTHOR  = 'lannocc'                     # name or alias of author
EMAIL   = 'lannocc@alphagriffin.com'    # email of author

URL     = 'http://alphagriffin.com'
LICENSE = 'AG'                          # type of license
COPY    = '2017 Alpha Griffin'          # copyright

CLASS   = [
    # @see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Topic :: System :: Logging',
    'Topic :: Utilities'
]


#
# END CUSTOMIZATION AREA
# -------------------------------------------------------------------------------------







#################
# !!! WARNING !!!
# !!! WARNING !!!
#################
# THINK CAREFULLY BEFORE CHANGING ANYTHING BELOW THIS LINE

from setuptools import setup, find_packages
from codecs import open
from os import path

def findversion(root, name):
    '''versioning strategy taken from http://stackoverflow.com/a/7071358/7203060'''

    import re
    vfile = path.join(root, name, "__version__.py")
    vmatch = re.search(r'^__version__ *= *["\']([^"\']*)["\']', open(vfile, "rt").read(), re.M)
    if vmatch:
        version = vmatch.group(1)
        print ("Found %s version %s" % (name, version))
        return version
    else:
        raise RuntimeError("Expecting a version string in %s." % (vfile))


if __name__ == '__main__':

    setup(

        name=NAME,
        version=findversion(NS, NAME),
        license=LICENSE,
        namespace_packages=[NS], # home for our libraries
        packages=find_packages(exclude=['tests']),
        author=AUTHOR,
        author_email=EMAIL,
        description=DESC,
        long_description=open('README.rst').read(),
        url=URL,
        classifiers=CLASS,
        keywords=TAGS,

        # run-time dependencies
        install_requires=REQUIRE,

        extras_require={
        },

        package_data={
        },

        data_files=[],

        entry_points={
        },
    )

