from setuptools import setup, find_packages

setup(
    name="Spectral",                              # Module name
    version="0.1.0",                              # Initial version
    description="A Python package for CASTEP post processing and plotting spectral plots",
    author="Zachary Hawkhead",
    author_email="zachary.hawkhead@gmail.com",
    url="https://github.com/zachary-hawk/Spectral.py.git", # GitHub URL
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "numpy",
        "ase>=3.18.1",
        "matplotlib",
        "cycler"
    ],
    classifiers=[
        "Programming Language :: Python :: 3"])
