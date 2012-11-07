from setuptools import setup, find_packages

setup(
    name="cmdtube",
    version="1.0",
    author="Mikkel Oscar Lyderik",
    author_email="mikkeloscar@gmail.com",
    license="GPL",
    platform="all",
    description="Simple commandline youtube search and player",
    scripts=['cmdtube'],
    packages=find_packages(),
)
