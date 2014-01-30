SF Python Testing
=================

This is the code for a testing talk I helped give at SF Python Meetup. It covers virtualenv, nose,
mock, monkey patching, dependency injection, and doctest.

  1. Getting everything setup with pip, virtualenv, etc.
  2. Using nose.
  3. Writing a test for code that should raise an exception.
  4. Testing using mock.patch.
  5. Testing using dependency injection.
  6. Testing with Doctest.

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
