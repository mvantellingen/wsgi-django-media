from django.conf import settings


def pytest_configure():
    settings.configure(
        MEDIA_URL='/media/',
        MEDIA_ROOT='tests/media/',
        HEALTH_CHECKS={},
        MIDDLEWARE_CLASSES=[],
        CACHES={
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                'LOCATION': 'unique-snowflake',
            }
        },
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite',
            },
        }
    )
