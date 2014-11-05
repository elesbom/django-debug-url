#
# encoding: utf-8

from setuptools import setup, find_packages

version = '0.1'

setup(name='django_debug_url',
      version=version,
      description="App for debug url",
      long_description="""\
App for debug url""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='debug url, view, django, middleware',
      author='elesbom',
      author_email='rafaelsantosg@gmail.com',
      url='https://github.com/elesbom/django-debug-url.git',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
