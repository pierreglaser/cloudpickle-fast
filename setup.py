import os
import pathlib
import re

from setuptools import setup, Extension, find_packages


pkg_root = pathlib.Path(os.path.dirname(__file__))

with open(pkg_root / 'README.rst', 'r') as fh:
    long_description = fh.read()


# Function to parse __version__ in `cloudpickle_fast/__init__.py`
def find_version():
    with open(pkg_root/'cloudpickle_fast'/'__init__.py', 'r') as fp:
        version_file = fp.read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


extra_compile_args = []
if os.name == 'posix':
    # Assume a gcc/clang-compatible CLI and enable C99 on old compilers
    extra_compile_args.append('-std=c99')

ext_modules = [
    Extension('cloudpickle_fast._pickle',
              ['cloudpickle_fast/_pickle.c'],
              extra_compile_args=extra_compile_args),
    ]

setup(
    name="cloudpickle_fast",
    version=find_version(),
    author="Pierre Glaser",
    author_email="pierre.glaser@msn.com",
    description="Experimental extension of the C pickle module",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/pierreglaser/cloudpickle_fast",
    packages=find_packages(),
    ext_modules=ext_modules,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
