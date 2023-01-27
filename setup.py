from sys import path
from subprocess import run
from setuptools import setup
from setuptools.command.install import install

class InstallPlaywrightDrivers(install):
    def run(self):
        run([path, "-m", "playwright", "install"], shell=True)
        install.run(self)

setup(install_requires=["playwright"], cmdclass={"install": InstallPlaywrightDrivers})
