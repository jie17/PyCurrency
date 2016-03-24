# Always prefer setuptools over distutils
from setuptools import setup, find_packages
setup(
  name = 'currency_calculator',
  packages = ['currency_calculator'], # this must be the same as the name above
  version = '0.1.2',
  description = 'A library to convert currency.',
  author = 'Jie Lu',
  author_email = 'jielu@msn.com',
  url = 'https://github.com/764664/PyCurrency', # use the URL to the github repo
  download_url = 'https://github.com/764664/PyCurrency', # I'll explain this in a second
  keywords = ['currency'], # arbitrary keywords
  classifiers = [],
)
