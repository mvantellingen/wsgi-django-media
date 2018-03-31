from setuptools import setup

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'pytest-cov>=2.2.0',
    'pytest-django>=3.0.0',
    'pytest>=2.8.3',
    'WebTest==2.0.23',

    # Linting
    'isort==4.2.5',
    'flake8==3.0.3',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==1.4.0',
]


setup(
    name='wsgi-django-media',
    version='1.0.0',
    description="WSGI middleware to serve media for faster Django development",
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/mvantellingen/wsgi-django-media',
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    install_requires=[
        'django>=1.8',
        'webob>=1.0.0',
    ],
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    package_dir={'': 'src'},
    py_modules=['wsgi_django_media'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=False,
)
