KAZ
===

.. image:: https://circleci.com/gh/attakei/kaz.svg?style=svg
    :target: https://circleci.com/gh/attakei/kaz

**KAZ** (Kit of AppImage Zoning) is portable AppImage manager for Desktop Linux users.

You can fetch, download and link AppImages that you want to use by CLI.


Installation
------------

KAZ is currently released only as GitHub repository.

.. code-block:: bash

   $ pip install https://github.com/attakei/kaz/archive/master.zip


Usage
-----

1. Initialize root directory and set envs

.. code-block:: bash

   $ kaz init ~/.kaz
   $ export KAZ_ROOT=$HOME/.kaz
   $ export PATH=$HOME/.kaz/bin:$PATH

2. Add application your local repository

.. code-block:: bash

   $ kaz add hyper '*.AppImage'

3. Download your app

   $ kaz pull hyper

4. Link your app to use from shell

   $ kaz link hyper 2.1.2
