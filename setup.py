#!/usr/bin/env python
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='github_token',
    packages=['github_token'],
    version='0.1.0',
    description='Library to create github personal auth token',
    long_description=readme(),
    author='Mario Corchero',
    author_email='mariocj89@gmail.com',
    url='https://github.com/Mariocj89/github_token',
    keywords=['github', 'authorization', 'tfa', 'token', 'twofactor'],
    license='MIT',
    test_suite='nose.collector',
    use_2to3=True,
    install_requires=['requests', 'enum34;python_version < "3.4"'],
    entry_points={
        'console_scripts': [
            'github_token=github_token.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
