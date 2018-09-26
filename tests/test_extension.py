import unittest
from unittest.mock import MagicMock, patch

from scrapy import signals
from scrapy.http import TextResponse
from twisted.python.failure import Failure

from sentry_scrapy.extension import SentryExtension


class SentryExtensionTestCase(unittest.TestCase):

    @patch('sentry_scrapy.extension.ignore_logger')
    def test_from_crawler(self, ignore_logger):
        crawler = MagicMock()
        extension = SentryExtension.from_crawler(crawler)
        self.assertIsInstance(extension, SentryExtension)
        crawler.signals.connect.assert_called_with(
            extension.spider_error,
            signal=signals.spider_error
        )
        ignore_logger.assert_called_with('scrapy.core.scraper')

    @patch('sentry_scrapy.extension.capture_exception')
    @patch('sentry_sdk.scope.Scope.set_tag')
    @patch('sentry_sdk.scope.Scope.set_extra')
    def test_spider_error(self, scope_set_extra, scope_set_tag, capture_exception):
        resp = TextResponse(
            'https://url.com',
            status=201,
            headers={'Content-type': 'text/html'},
            body=b'<!doctype><html><body><p>test</p></body></html>'
        )
        error = Exception('Boom')
        failure = Failure(error)
        spider = MagicMock()
        spider.name = 'superspider'
        SentryExtension.spider_error(failure, resp, spider)

        scope_set_tag.assert_called_with('spider', 'superspider')
        scope_set_extra.assert_called_with('response', {
            'status': 201,
            'url': 'https://url.com',
            'headers': {'content-type': 'text/html'},
            'body': '<!doctype><html><body><p>test</p></body></html>',
        })
        capture_exception.assert_called_with(error)
