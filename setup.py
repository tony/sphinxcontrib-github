"""
sphinxcontrib-github
~~~~~~~~~~~~~~~~~~~~

github directives and roles for sphinx.


Links
-----

* `github repository <https://www.github.com/tony/sphinxcontrib-github>`_

"""
from setuptools import setup, find_packages
try:
    from pip.req import parse_requirements
except ImportError:
    def requirements(f):
        reqs = open(f, 'r').read().splitlines()
        reqs = [r for r in reqs if not r.strip().startswith('#')]
        return reqs
else:
    def requirements(f):
        install_reqs = parse_requirements(f)
        reqs = [str(r.req) for r in install_reqs]
        return reqs


setup(
    name='sphinxcontrib-github',
    version='0.1.2',
    url='https://github.com/tony/sphinxcontrib-github/',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-github',
    license='BSD',
    author='Tony Narlock',
    author_email='tony@git-pull.com',
    description='github directives and roles for sphinx',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=find_packages(),
    install_requires=requirements('requirements.pip'),
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
