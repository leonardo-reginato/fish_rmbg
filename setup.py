from setuptools import setup, find_packages

# Package metadata
NAME = "fish-bg-extractor"
VERSION = "0.1.0"
DESCRIPTION = "Application to remove the background of a fish images"
URL = "https://github.com/leonardo-reginato/FishBGExtractor.git"
AUTHOR = "Leonardo F Reginato"
EMAIL = "leonardofonseca.r@gmail.com"
LICENSE = "MIT"  # Choose the appropriate license

# Package dependencies
with open("requirements.txt") as f:
    INSTALL_REQUIRES = f.read().splitlines()

# Long description (from README.md)
with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# Other classifiers (https://pypi.org/classifiers/)
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

# Package setup
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    entry_points={
        "console_scripts": ["fish_bg_app = fish_bg_extractor.app_bg_extractor:main"]
    },
)
