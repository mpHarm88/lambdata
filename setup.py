"""
Lambdata - a collection of data science helper finctions for lambda school
"""

import setuptools

REQUIRED = [
        "numpy",
        "pandas"
        ]

with open("README.md", "r") as fh:
    LONG_DESCRIPTON = fh.read()
    setuptools.setup(
            name="lambdata-mpharm88",
            version="0.1.6",
            author="mpharm88",
            description="a collection of data science helper functions",
            long_description=LONG_DESCRIPTON,
            long_description_content_type="text/markdown",
            url="https://github.com/mpHarm88/lambdata",
            packages=setuptools.find_packages(),
            python_requires=">=3.5",
            install_requires=REQUIRED,
            classifiers=["Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
             ]
            )
