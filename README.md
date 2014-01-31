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

See Also
--------

About nose:

  https://nose.readthedocs.org/en/latest/

This post, although not perfect, is a useful introduction to mock:

  http://www.toptal.com/python/an-introduction-to-mocking-in-python

Dependency Injection in Python:

  http://www.aleax.it/yt_pydi.pdf

See "Make Some Strong Statements" in the link for some strong and fun opinions on testing:

  https://raw.github.com/jjinux/pyteladventure/master/pybdd_talk.txt
