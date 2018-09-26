#!/usr/bin/env python

from setuptools import setup, find_packages


VERSION = '0.1'


setup(
    name='sentry-scrapy',
    version=VERSION,
    description='Scrapy integration with Sentry SDK (unofficial)',
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
