from setuptools import setup

'''
Flask-OpenTracing
-----------------

This extension provides simple integration of OpenTracing in Flask applications.
'''
version = open('VERSION').read().strip()
setup(
    name='Flask-OpenTracing',
    version=version,
    url='http://github.com/opentracing-contrib/python-flask',
    download_url='https://github.com/opentracing-contrib/python-flask/tarball/'+version,
    license='BSD',
    author='Kathy Camenzind',
    author_email='kcamenzind@lightstep.com',
    description='OpenTracing support for Flask applications',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    packages=['flask_opentracing', 'tests'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'opentracing>=2.0,<3',
    ],
    extras_require={
        'tests': [
            'flake8',
            'flake8-quotes',
            'mock',
            'pytest',
            'pytest-cov',
            'tox',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
