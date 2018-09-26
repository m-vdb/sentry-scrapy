"""Utils module."""


def response_to_dict(response):
    """
    Convert a `scrapy.http.Response` to a dictionnary.
    """
    return {
        'status': response.status,
        'url': response.url,
        'headers': response.headers.to_unicode_dict(),
        'body': response.text,
    }
