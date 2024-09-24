from setuptools import setup, find_packages

setup(
    name="zetapy",
    version="3.0.7",
    description="Implementations of the ZETA family of statistical tests.",
    author="Jorrit Montijn, Guido Meijer & Alexander Heimel",
    packages=find_packages(),
    install_requires=[
        "matplotlib", 
        "numpy", 
        "scipy"
    ]
)
