import logging
import os

from django.conf import settings
from webob import Request
from webob.static import FileApp

__version__ = '1.0.0'


def DjangoMedia(app):
    """WSGI Middleware for Django development purposes only.

    :param app: the wsgi application

    """
    if not settings.DEBUG or not settings.MEDIA_URL.startswith('/'):
        return app

    logging.info(
        "Serving media files at %s from %s",
        settings.MEDIA_URL, settings.MEDIA_ROOT)

    document_root = os.path.realpath(settings.MEDIA_ROOT)

    def wrapper(environ, start_response):
        request = Request(environ)
        if request.path.startswith(settings.MEDIA_URL):

            filename = request.path[len(settings.MEDIA_URL):]
            path = os.path.realpath(os.path.join(document_root, filename))
            if path.startswith(document_root):
                return FileApp(path)(environ, start_response)
        return app(environ, start_response)

    return wrapper
