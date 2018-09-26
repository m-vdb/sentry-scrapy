"""Scrapy extension."""
from scrapy import signals
from sentry_sdk import push_scope, capture_exception
from sentry_sdk.integrations.logging import ignore_logger

from .utils import response_to_dict


class SentryExtension:
    """
    Scrapy extension that uses Sentry to log errors.
    """
    @classmethod
    def from_crawler(cls, crawler):
        """
        Initialize the extension from a crawler instance and connect
        to the `spider_error` signal.
        """
        extension = cls()
        crawler.signals.connect(extension.spider_error, signal=signals.spider_error)

        # ignore sentry logger
        ignore_logger('scrapy.core.scraper')

        return extension

    @staticmethod
    def spider_error(failure, response, spider):
        """
        This function is used as a callback to the `spider_error` signal.

        :param failure:        the exception raised
        :param response:       the response being processed when the exception was raised
        :param spider:         the spider which raised the exception
        """
        # update sentry scope on the fly
        with push_scope() as scope:
            scope.set_tag('spider', spider.name)
            scope.set_extra('response', response_to_dict(response))
            # catch the exception
            capture_exception(failure.value)
