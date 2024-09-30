from setuptools import setup, find_packages
from setuptools import find_packages

setup(
    name='ektabuild',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
            'Jinja2==3.1.4',
            'MarkupSafe==2.1.5',
            'PyYAML==6.0.2',
            'pytest==7.0.1',
        ],
    entry_points={
        'console_scripts': [
            'ektabuild=ektabuild.main:main',
        ],
    },
)