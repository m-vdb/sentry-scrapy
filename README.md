# sentry-scrapy

[![Build Status](https://travis-ci.org/m-vdb/sentry-scrapy.svg?branch=master)](https://travis-ci.org/m-vdb/sentry-scrapy)
[![Coverage Status](https://coveralls.io/repos/github/m-vdb/sentry-scrapy/badge.svg?branch=master)](https://coveralls.io/github/m-vdb/sentry-scrapy?branch=master)
[![Pypi version](https://img.shields.io/pypi/v/sentry-scrapy.svg)](https://pypi.python.org/pypi/sentry-scrapy)

Scrapy integration with latest Sentry SDK


## Requirements

- Python3
- [`Scrapy`](https://docs.scrapy.org/en/latest/)
- [`sentry-sdk`](https://docs.sentry.io/quickstart?platform=python)

## Installation

Install with `pip`:

```bash
$ pip install sentry-scrapy
```

And in your Scrapy settings, configure Sentry as follows:

```python

# configure the extensions
# https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "sentry_scrapy.extension.SentryExtension": 10,
}

# initialize Sentry
# https://docs.sentry.io/quickstart?platform=python
import sentry_sdk
sentry_sdk.init(dsn='your dsn')
```
