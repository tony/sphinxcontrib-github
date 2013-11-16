Show of github repos and pull requests in your sphinx resume / project.

.. image:: https://badge.fury.io/py/sphinxcontrib-github.png
    :target: http://badge.fury.io/py/sphinxcontrib-github

Installation
------------

.. code-block:: bash

    $ pip install sphinxcontrib-github

Add sphinxcontrib-github to your ``extensions`` in ``conf.py``.

.. code-block:: python

    extensions.append('sphinxcontrib.github')

or change:

.. code-block:: python

    extensions = ['sphinx.ext.intersphinx', ...]

to:

.. code-block:: python

    extensions = ['sphinx.ext.intersphinx', 'sphinxcontrib.github', ...]


Setting up API access
---------------------

First use will require entering your github username and password. Read
the `source for logging in`_. It will create an API key with github and
save an api id and api key for future usage in your projects directory.

Add ``.github.auth`` to your ``.gitignore``.

Usage
-----

github pull request role
""""""""""""""""""""""""

.. code-block:: rest

    :github-pr:`saltstack/salt/pull/7665`

output:

`salt`_ (`#7665`_) *Fixed tags for progress events and preload*

.. _salt: https://www.github.com/saltstack/salt
.. _#7665: https://www.github.com/saltstack/salt/pull/7665

24 additions(+), 12 deletion(-) 2013-10-08

github repo role
""""""""""""""""

.. code-block:: rest

    :github-repo:`saltstack/salt`

output:

salt-states-configs: `github`_

github repo directive
"""""""""""""""""""""

.. code-block:: rest

    .. github-repo:: saltstack/salt
        :homepage: http://www.saltstack.org/
        :travis: https://www.travis-ci.org/saltstack/salt/
        :docs: http://salt.readthedocs.org/en/v0.16.4/
        :api: http://salt.readthedocs.org/en/v0.16.4/ref/python-api.html
        :pypi: https://pypi.python.org/pypi/salt

output:

`github`_ - `travis`_ - `docs`_ - `api`_ - `pypi`_ - `homepage`_ - 2296 watchers - 813 forks

==============  ==========================================================
python support  2.7
sphinx support  >=0.6
Docs            http://sphinxcontrib-github.rtfd.org
API             http://sphinxcontrib-github.readthedocs.org/en/latest/api.html
Changelog       http://sphinxcontrib-github.readthedocs.org/en/latest/history.html
Issues          https://github.com/tony/sphinxcontrib-github/issues
Source          https://github.com/tony/sphinxcontrib-github
pypi            https://pypi.python.org/pypi/sphinxcontrib-github
License         `BSD`_.
==============  ==========================================================


.. _homepage: http://www.saltstack.org
.. _github: https://www.github.com/saltstack/salt
.. _docs: http://salt.readthedocs.org/en/v0.16.4/
.. _api: http://salt.readthedocs.org/en/v0.16.4/ref/python-api.html
.. _travis: http://www.travis-ci.org/saltstack/salt
.. _pypi: https://pypi.python.org/pypi/salt
.. _BSD: http://opensource.org/licenses/BSD-3-Clause

.. _source for logging in: https://github.com/tony/sphinxcontrib-github/blob/master/sphinxcontrib/github.py#L40
