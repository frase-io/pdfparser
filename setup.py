import sys

from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


class Test(TestCommand):
    def run_tests(self):
        import pytest
        errno = pytest.main([])
        sys.exit(errno)


setup(
    name="pdfparser",
    version="1.0.0",
    author="Bryant Moscon",
    author_email="bmoscon@gmail.com",
    description=("pdf parsing tools"),
    packages=find_packages(exclude=['tests']),
    cmdclass={'test': Test},
    tests_require=["pytest"],
    install_requires=[
        "pdftotext"
    ],
)
