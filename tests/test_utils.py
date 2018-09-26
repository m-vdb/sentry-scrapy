import unittest

from scrapy.http import Response

from sentry_scrapy import utils


class UtilsTestCase(unittest.TestCase):

    def test_response_to_dict(self):
        resp = Response(
            'https://url.com',
            status=201,
            headers={'Content-type': 'text/html'},
            body=b'<!doctype><html><body><p>test</p></body></html>'
        )
        self.assertEqual(utils.response_to_dict(resp), {
            'status': 201,
            'url': 'https://url.com',
            'headers': {'content-type': 'text/html'},
            'body': b'<!doctype><html><body><p>test</p></body></html>',
        })
