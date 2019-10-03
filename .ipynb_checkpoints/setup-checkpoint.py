
from setuptools import setup

setup(name='stream_faust',
      version='0.1',
      description='A simple library for dealing with stram datas.',
      url='https://github.com/ajay1993/stream_faust.py',
      author='Ajay S Nair',
      author_email='ajays4u.nair@gmail.com',
      license='MIT',
      packages=['stream_faust'],
      install_requires=[
          'fuzzywuzzy',
          'pandas', 
          'faust',
          'datetime'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
