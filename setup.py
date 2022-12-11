import os
from setuptools import find_packages, setup


def read(fpath):
    """Reads a file within package directories"""
    with open(os.path.join(os.path.dirname(__file__), fpath)) as f:
        return f.read()


setup(
    name='django-base-app',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Provides static files and base HTML laytout',
    long_description=read('README.md'),
    url='http://www.codingwithalex.com',
    author='Alex Silva',
    author_email='alex@codingwithalex.com',
    python_requires='>=3',
    zip_safe=False,
    install_requires=[
        'django==4.1.4'
    ]
)
