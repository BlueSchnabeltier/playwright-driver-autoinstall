from sys import executable
from setuptools import setup
from subprocess import check_output
from setuptools.command.install import install

class InstallPlaywrightDrivers(install):
    def run(self):
        check_output([executable, "-m", "install", "playwright"])
        install.run(self)

setup(name="playwright-driver-autoinstall", install_requires=["playwright"], cmdclass={"install": InstallPlaywrightDrivers})
