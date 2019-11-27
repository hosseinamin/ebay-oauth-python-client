from setuptools import setup


setup(
    name="ebay-oauth-python-client",
    version="0.0.1",
    packages=['ebayoauthclient'],
    license="LICENSE.txt",
    description="Python OAuth SDK: Get OAuth tokens for eBay public APIs",
    author="Hossein Amin",
    url="https://github.com/hosseinamin/ebay-oauth-python-client",
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'selenium>=3.141.0,<4',
        'requests>=2.21.0,<3',
        'PyYAML>=5.1,<6',
    ]
)
