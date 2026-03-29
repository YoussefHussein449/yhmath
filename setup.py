from setuptools import setup, find_packages

setup(
    name="yhmath",                 
    version="1.0.2",                  
    packages=find_packages(),       
    install_requires=[              
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "yhmath = yhmath.__main__:main",
        ],
    },
    description="A math python package ",
    author="Youssef Hussein",
)