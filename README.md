SF Python Testing
=================

This is a lightning quick introduction to virtualenv, nose, mock, monkey patching, dependency
injection, and doctest. See the blog post:

  http://jjinux.blogspot.com/2014/01/python-lightning-quick-introduction-to.html

I first presented this material at SF Python Meetup, hence the name of the repository.

Setup
-----

    # Make sure you're using the version of Python you want to use.
    which python

    sudo easy_install -U setuptools
    sudo easy_install pip
    sudo pip install virtualenv
    mkdir ~/Desktop/sfpythontesting
    cd ~/Desktop/sfpythontesting
    virtualenv env

    # Do this anytime you want to work on the application.
    . env/bin/activate

    # Make sure that pip is running from within the env.
    which pip

    # Previously ran:
    # pip install nose
    # pip install mock
    # pip freeze > requirements.txt
    pip install -r requirements.txt

Running Tests
-------------

    nosetests --with-doctest
