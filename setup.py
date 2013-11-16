"""
sphinxcontrib-github
~~~~~~~~~~~~~~~~~~~~

github directives and roles for sphinx.


Links
-----

* `github repository <https://www.github.com/tony/sphinxcontrib-github>`_

"""
from setuptools import setup, find_packages

with open('requirements.pip') as f:
    install_reqs = [line for line in f.read().split('\n') if line]
    tests_reqs = []

setup(
    name='sphinxcontrib-github',
    version='0.1.3',
    url='https://github.com/tony/sphinxcontrib-github/',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-github',
    license='BSD',
    author='Tony Narlock',
    author_email='tony@git-pull.com',
    description='github directives and roles for sphinx',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=find_packages(),
    install_requires=install_reqs,
    namespace_packages=['sphinxcontrib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
)
