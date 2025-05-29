# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


dependencies = [dependency.strip()
                for dependency in open("requirements.txt").readlines()]

setup(
    name='efipay',

    version='1.0.4',

    description='Module for integration with EfiPay API',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/efipay/sdk-python-apis-efi',

    # Author details
    author='Consultoria Técnica',
    author_email='consultoria@sejaefi.com.br',

    # Choose your license
    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],

    # What does your project relate to?
    keywords='payment EfiPay',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['pytest-cov', 'pytest', 'responses'],
    },

    package_data={
    '': ['requirements.txt', 'README.md', 'LICENSE']
    },

    include_package_data=True,

    install_requires=dependencies,
)
