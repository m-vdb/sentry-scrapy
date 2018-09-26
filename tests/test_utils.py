import json
import unittest

from scrapy.http import TextResponse

from sentry_scrapy import utils


class UtilsTestCase(unittest.TestCase):

    def test_response_to_dict(self):
        resp = TextResponse(
            'https://url.com',
            status=201,
            headers={'Content-type': 'text/html'},
            body=b'<!doctype><html><body><p>test</p></body></html>'
        )
        resp_dict = utils.response_to_dict(resp)
        self.assertEqual(resp_dict, {
            'status': 201,
            'url': 'https://url.com',
            'headers': {'content-type': 'text/html'},
            'body': '<!doctype><html><body><p>test</p></body></html>',
        })
        try:
            json.dumps(resp_dict)
        except (ValueError, TypeError) as error:
            self.fail('Response dict is not JSON serializable: {}'.format(error))
