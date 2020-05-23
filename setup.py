from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="python_debug",
    version="0.0.2",
    author="D-Bhatta",
    author_email="dbhatta1232@gmail.com",
    description="Following the code for the Python Debugging with PDB tutorial on Real Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/D-Bhatta/Python-Debugging.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
