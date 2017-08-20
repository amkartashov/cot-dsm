from setuptools import setup

setup(
    name='dsm',
    packages=['dsm'],
    include_package_data=True,
    install_requires=[
        'flask',
        'docker',
    ],
)
