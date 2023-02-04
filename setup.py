from sys import executable
from subprocess import call
from setuptools import setup
from setuptools.command.install import install

class InstallPlaywrightDrivers(install):
    def run(self):
        call([executable, "-m", "playwright", "install"])
        install.run(self)

setup(name="playwright-driver-autoinstall", install_requires=["playwright"], cmdclass={"install": InstallPlaywrightDrivers})
