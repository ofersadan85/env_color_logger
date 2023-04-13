from pathlib import Path

from setuptools import setup

long_description = Path(__file__).with_name("README.md").read_text(encoding="utf-8")
requirements = Path(__file__).with_name("requirements.txt").read_text().split()

setup(
    name="env_color_logger",
    version="0.0.3",
    packages=["env_color_logger"],
    url="https://github.com/ofersadan85/env_color_logger",
    license="MIT License",
    author="Ofer Sadan",
    author_email="ofersadan85@gmail.com",
    description="Simple logging using env variables",
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True,
)
