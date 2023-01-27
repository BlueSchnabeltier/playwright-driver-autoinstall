from sys import path
from setuptools import setup
from subprocess import check_output
from setuptools.command.install import install

class InstallPlaywrightDrivers(install):
    def run(self):
        check_output([path, "-m", "install", "playwright"], shell=True)
        install.run(self)

setup(install_requires=["playwright"], cmdclass={"install": InstallPlaywrightDrivers})
