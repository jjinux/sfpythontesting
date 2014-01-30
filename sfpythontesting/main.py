import random


def sum(a, b):
  return a + b


def raise_an_exception():
  raise ValueError("This is a ValueError")


def make_a_move_with_mock_patch():
  """Figure out what move to make in a hypothetical game.

  Use random.randint in part of the decision making process.

  In order to test this function, you have to use mock.patch to monkeypatch random.randint.

  """
  if random.randint(0, 1) == 0:
    return "Attack!"
  else:
    return "Defend!"


def make_a_move_with_dependency_injection(randint=random.randint):
  """This is another version of make_a_move.

  Accept the randint *function* as a parameter so that the test code can inject a different
  version of the randint function.

  This is known as dependency injection.

  """
  if randint(0, 1) == 0:
    return "Attack!"
  else:
    return "Defend!"


def hello_doctest(name):
  """This is a Hello World function for using Doctest.

  >>> hello_doctest("JJ")
  'Hello, JJ!'

  """
  return "Hello, %s!" % name
