from setuptools import setup

config = {
    'description': 'Max Sum',
    'author': "Arun Tiwari",
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'arunstiwari@gmail.com',
    'version': '0.1',
    'packages': ['maxsum'],
    'scripts': [],
    'name': 'maxsum'
}

setup(**config,
    setup_requires = ['pytest-runner'],
    tests_require  = ['pytest']
)
