#!/usr/bin/env python
import sys
from distutils.core import setup

from filechunkio import __version__

PY3 = sys.version_info[0] == 3

_unicode = str if PY3 else unicode

setup(
    name="filechunkio",
    version=_unicode(__version__),
    description="FileChunkIO represents a chunk of an OS-level file "\
        "containing bytes data",
    long_description=open("README", 'r').read(),
    author="Fabian Topfstedt",
    author_email="topfstedt@schneevonmorgen.com",
    url="http://bitbucket.org/fabian/filechunkio",
    license="MIT license",
    packages=["filechunkio"],
)
