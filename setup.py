#!/usr/bin/env python

from setuptools import setup, find_packages


VERSION = '0.2'

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='sentry-scrapy',
    version=VERSION,
    description='Scrapy integration with Sentry SDK (unofficial)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Maxime Vdb',
    author_email='me@maxvdb.com',
    packages=find_packages(),
    install_requires=['Scrapy', 'sentry-sdk'],
    license="MIT",
    keywords="sentry scrapy sdk integration",
    url='https://github.com/m-vdb/sentry-scrapy',
    download_url='https://github.com/m-vdb/sentry-scrapy/archive/v{}.tar.gz'.format(VERSION),
    project_urls={
        "Source Code": "https://github.com/m-vdb/sentry-scrapy",
    }
)
