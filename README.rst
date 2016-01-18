===========
Hapydeis
===========

A Python thin wrapper around deis api, for now only provide a level 0 client (which should be improved with a couple
of new features quite soon)

Installation
============

::

    pip install git+https://github.com/Grindizer/hapydeis#egg=hapydeis

Or in a develop mode after downloading a zip or cloning the git repository ::

    git clone https://github.com/Grindizer/hapydeis
    cd hapydeis
    pip install -e .

Or in a develop mode from a git repository ::

    pip install -e git+https://github.com/Grindizer/hapydeis#egg=hapydeis

Usage
=====

::

    from hapydeis import Client
    mycluster = Client('http://deis.mycluster.example.com')
    mycluster.authenticate('user', 'just an example here')
    list_apps = mycluster.apps.get()

Development
===========

To run the all tests run ::

    py.test

