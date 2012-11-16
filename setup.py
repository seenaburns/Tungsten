import tungsten
from distutils.core import setup

setup(
    name='Tungsten',
    version=tungsten.__version__,
    author='Seena Burns',
    author_email='hello@ethanbird.com',
    url='https://github.com/seenaburns/Tungsten',
    license=open('LICENSE.txt').read(),
    description='Wolfram Alpha API built for Python.',
    long_description=open('README.md').read() + '\n\n' + 
                     open('HISTORY.md').read(),   
    packages={'tungsten': 'tungsten'},
    package_data={'': ['LICENSE.txt']},
    install_requires=[
        'requests >= 0.14.1',
    ],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
)
