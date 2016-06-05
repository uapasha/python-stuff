try:
	from setuptools import setup
except ImportError:
	from distutils.cpre import setuptools

config = {
	'description': 'My project',
	'author': 'Paul',
	'url': 'URL to get it all',
	'download_url': 'Where to download it',
	'author_email': 'uapasha@ukr.net',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'skeleton'
}

setup (**config)