auxtest
=======

|python| |Build Status| |Coverage|

Production code of auxtest.


Setup
=====
It is highly recommended to develop this project in a virtual environment.

Example for starting and using a virtual environment (you are free to use your own/preferred setup):

.. code-block:: bash

  auxtest$ pip install virtualenv
  auxtest$ virtualenv env -p python3.7
  auxtest$ source env/bin/activate


Building a package
==================
Building a package can be done with pip:

.. code-block:: bash

  auxtest$ pip wheel -w wheel --no-index --no-deps .

To use it, install it into some virtual environment and import it:

.. code-block:: bash

  auxtest$ pip install wheel/*
  auxtest$ python
  auxtest >>> import auxtest
  auxtest >>> # here we go!

Building a docker container
===========================
You'll need docker in order to build and run a container, and the auxtest-wheel needs to be built and in place:

.. code-block:: bash

  auxtest$ docker build . -t auxtest:latest
  auxtest$ docker run -p 5000:5000 auxtest:latest

With the current settings, the dev server will run, which will also tell you where it can be reached.

TODO
====

If you want the shiny badges (currently only for pipeline status and coverage) on your project page in gitlab, update the links at the bottom of this document to point to the right gitlab domain.


Tools
=====
This section lists all tools, gives a short explanation of their purpose and the command to install and run them locally. If they are part of the buildchain, they will also indicate whether they should be voting or not.

All the dependencies for these tools can also be installed by running ``pip install -r requirements-dev.txt``.


pytest
------

(*build chain, voting*)

`pytest`_ runs the unit test suite by searching functions that start with ``test_``, or a few other criteria that we don't use. For details, see `autodetection`_.

Local install:

.. code-block:: bash

  auxtest$ pip install pytest
  auxtest$ pip install -e .  # treat your project as a package, adding `src` to the code base

Usage:

.. code-block:: bash

  auxtest$ pytest


flake8
------

(*build chain, voting*)

`flake8`_ is the linter for this project. We want it to enforce the rules similar to those defined by `hacking`_, minus the parts that we don't like.

Local install:

.. code-block:: bash

  auxtest$ pip install pep8-naming flake8 flake8-docstrings flake8-import-order

Usage:

.. code-block:: bash

  auxtest$ flake8 src tests


mypy
----

(*build chain, voting*)

`mypy`_ is an optional static type checker that behaves pretty much like a linter. If you use `PEP 484`_ style type hinting, running mypy regularly is a good idea.

Local install:

.. code-block:: bash

  auxtest$ pip install mypy

Usage:

.. code-block:: bash

  auxtest$ mypy src --ignore-missing-imports


coverage
--------

(*build chain, non voting*)

`coverage`_ is our test-coverage reporting tool of choice. It is understood to be read-only, since code coverage is a very weakly defined criterion. Since it runs unit tests to compute coverage, it depends on ``pytest`` as well.

Local install:

.. code-block:: bash

  auxtest$ pip install pytest, coverage
  auxtest$ pip install -e .  # if you haven't done this for pytest already

Usage:

.. code-block:: bash

  auxtest$ coverage erase
  auxtest$ coverage run -m pytest &> /dev/null
  auxtest$ coverage combine &> /dev/null
  auxtest$ coverage report --omit=*/__init__.py,*/__main__.py,*/settings.py,*/logging.py -m


sphinx
------

(*build chain, non voting*)

`sphinx`_ builds the project's documentation from docstring. It is build as html by default so that it can be easily picked up by serving tools like `readthedocs`_ or `gitlab-pages`_. A different option that might be of interest would be to build with the LaTeX-builder to pdf.

Local install:

.. code-block:: bash

  auxtest$ pip install sphinx

Usage:

.. code-block:: bash

  auxtest$ sphinx-apidoc -f -o docs src/auxtest
  auxtest$ sphinx-build docs build/html
  #  or `sphinx-build doc build/pdf -b latex`

.. _pytest: https://docs.pytest.org/en/latest/
.. _flake8: http://flake8.pycqa.org/en/latest/index.html
.. _mypy: http://mypy-lang.org/
.. _coverage: https://coverage.readthedocs.io/en/coverage-4.5.1/
.. _sphinx: http://www.sphinx-doc.org/en/master/
.. _PEP 484: https://www.python.org/dev/peps/pep-0484/
.. _readthedocs: https://readthedocs.org/
.. _gitlab-pages: https://about.gitlab.com/features/pages/
.. _hacking: https://docs.openstack.org/hacking/latest/user/hacking.html
.. _autodetection: https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery
.. _your gitlab account: https://<gitlab-domain>.com/profile/account


.. |python| image:: https://img.shields.io/badge/python-3.6-brightgreen.svg
   :target: https://pypi.python.org/pypi/auxtest/

.. |Build Status| image:: https://<gitlab_domain>/auxtest/badges/master/pipeline.svg
   :target: https://<gitlab-domain>.com/labor/auxtest/commits/master

.. |Coverage| image:: https://<gitlab_domain>/auxtest/badges/master/coverage.svg
   :target: https://<gitlab-domain>.com/labor/auxtest/commits/master
