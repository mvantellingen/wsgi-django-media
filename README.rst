=================
WSGI Django Media
=================

Really simple wsgi middleware to serve media files before hitting the Django
app. Only enabled when Django DEBUG is True. This can really speed up your
local development process when a page loads a lot of media files.


Status
------

.. image:: https://readthedocs.org/projects/wsgi-django-media/badge/?version=latest
    :target: https://readthedocs.org/projects/wsgi-django-media/

.. image:: https://travis-ci.org/mvantellingen/wsgi-django-media.svg?branch=master
    :target: https://travis-ci.org/mvantellingen/wsgi-django-media

.. image:: http://codecov.io/github/mvantellingen/wsgi-django-media/coverage.svg?branch=master
    :target: http://codecov.io/github/mvantellingen/wsgi-django-media?branch=master

.. image:: https://img.shields.io/pypi/v/wsgi-django-media.svg
    :target: https://pypi.python.org/pypi/wsgi-django-media/


Getting started
===============

Using this module is really simple.  In Django for example edit the wsgi.py
file and add the following to the end of the file.

.. code-block:: python

  from wsgi_django_media import DjangoMedia
  application = DjangoMedia(application)


Installation
============

You can install the latest version using pip::

    pip install wsgi-django-media

