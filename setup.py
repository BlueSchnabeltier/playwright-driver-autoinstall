from sys import executable
from subprocess import call
from setuptools import setup
from setuptools.command.install import install

class InstallPlaywrightDrivers(install):
    def run(self):
        call([executable, "-m", "playwright", "install", "chromium"])
        call([executable, "-m", "playwright", "install", "firefox"])
        call([executable, "-m", "playwright", "install", "webkit"])
        install.run(self)

setup(name="playwright-driver-autoinstall", version="1.0", install_requires=["playwright"], cmdclass={"install": InstallPlaywrightDrivers})
