import tungsten
from distutils.core import setup

setup(
    name='Tungsten',
    version=tungsten.__version__,
    author='Seena Burns',
    author_email='hello@ethanbird.com',
    url='https://github.com/seenaburns/Tungsten',
    packages={'tungsten': 'tungsten'},
    license=open('LICENSE.txt').read(),
    description='Wolfram Alpha API built for Python.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests",
    ],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
)
