import setuptools
from distutils.core import setup

setup(
  name='instauto',
  packages=setuptools.find_packages(),
  version='1.0.4',
  license='MIT',
  description='Python wrapper for the private Instagram API',
  author='Stan van Rooy',
  author_email='stan@rooy.dev',
  url='https://github.com/stanvanrooy/instauto',
  download_url='https://github.com/stanvanrooy/instauto/archive/1.0.3.tar.gz',
  keywords=['instagram api', 'private instagram api'],
  install_requires=[
          'requests',
          'apscheduler',
          'pycryptodomex',
          'imagesize'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)  ',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.6'
  ],
)
