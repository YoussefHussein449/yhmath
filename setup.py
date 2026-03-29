from setuptools import setup, find_packages
from pathlib import Path

# Läs long_description från README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="yhmath",
    version="1.1.2",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "yhmath = yhmath.__main__:main",
        ],
    },
    description="A math python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Youssef Hussein",
    url="https://github.com/YoussefHussein449/yhmath",
    license="BSD 2-Clause",
    python_requires=">=3.6, <=3.12",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    math, yhmath, addition, numbers, arithmetic, calculator"
)
