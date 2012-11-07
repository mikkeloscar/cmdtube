from setuptools import setup, find_packages

setup(
    name="cmdtube",
    version="0.1",
    author="Mikkel Oscar Lyderik",
    author_email="mikkeloscar@gmail.com",
    license="GPL",
    platform="all",
    description="Simple commandline youtube search and play",
    scripts=['cmdtube'],
    packages=find_packages(),
)
