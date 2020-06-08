from setuptools import setup

setup(
    name='unats',
    version="0.0.1",
    description='NATS client for MicroPython',
    long_description='MicroPython client for NATS.io',
    classifiers=[
        'Intended Audience :: Developers',
        ],
    url='https://github.com/nats-io/unats.py',
    author='Waldemar Quevedo',
    author_email='wally@nats.io',
    license='Apache 2 License',
    packages=['unats'],
    zip_safe=True,
 )
