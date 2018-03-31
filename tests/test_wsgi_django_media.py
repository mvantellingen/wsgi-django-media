from webtest import TestApp as _TestApp

import wsgi_django_media


def wsgi_app(environ, start_response):
    body = b'No no no'
    headers = [
        ('Content-Type', 'text/html; charset=utf8'),
        ('Content-Length', str(len(body)))
    ]
    start_response('404 Not Found', headers)
    return [body]


def test_found_file_debug(monkeypatch, settings):
    settings.DEBUG = True

    application = wsgi_django_media.DjangoMedia(wsgi_app)
    app = _TestApp(application)
    response = app.get('/media/test.txt', status=200)
    assert response.unicode_body.strip() == "Yes, it works yes"


def test_found_file_no_escape(monkeypatch, settings):
    settings.DEBUG = True

    application = wsgi_django_media.DjangoMedia(wsgi_app)
    app = _TestApp(application)
    response = app.get('/media/../conftest.py', status=404)
    assert response.unicode_body.strip() == "No no no"


def test_found_file_prod(monkeypatch, settings):
    settings.DEBUG = False

    application = wsgi_django_media.DjangoMedia(wsgi_app)
    app = _TestApp(application)
    response = app.get('/media/test.txt', status=404)
    assert response.unicode_body.strip() == "No no no"


def test_debug_external(monkeypatch, settings):
    settings.DEBUG = True
    settings.MEDIA_URL = 'http://localhost/'

    application = wsgi_django_media.DjangoMedia(wsgi_app)
    app = _TestApp(application)
    response = app.get('/media/test.txt', status=404)
    assert response.unicode_body.strip() == "No no no"
