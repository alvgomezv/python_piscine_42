from setuptools import setup, find_packages

setup(
    name="my-minipack",
    version="1.0.0",
    description="How to create a package in Python.",
    author="alvgomez",
    author_email="alvgomez@student.42malaga.com",
    license="GPLv3",
    url=None,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Education",
        "Topic :: How To",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
)