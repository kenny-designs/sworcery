try:
	from setuptool import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'A simple platformer with art inspired by the game "Sword and Sworcery." ',
	'author': 'Alexander Aguilar',
	'url': 'None',
	'download_url': 'None',
	'author_email': 'alexanderman2004@yahoo.com',
	'version': '0.1',
	'install_requires': '['nose']',
	'packages': ['sworcery'],
	'scripts': [],
	'name': 'Sworcery'
}

setup(**config)