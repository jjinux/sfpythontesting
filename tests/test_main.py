from nose.tools import assert_equal, assert_raises
import mock

from sfpythontesting import main


def test_sum():
  assert_equal(main.sum(1, 2), 3)


def test_raise_an_exception():
  with assert_raises(ValueError) as context:
    main.raise_an_exception()
  assert_equal(str(context.exception), "This is a ValueError")


@mock.patch("sfpythontesting.main.random.randint")
def test_make_a_move_with_mock_patch_can_attack(randint_mock):
  randint_mock.return_value = 0
  assert_equal(main.make_a_move_with_mock_patch(), "Attack!")


@mock.patch("sfpythontesting.main.random.randint")
def test_make_a_move_with_mock_patch_can_defend(randint_mock):
  randint_mock.return_value = 1
  assert_equal(main.make_a_move_with_mock_patch(), "Defend!")


def test_make_a_move_with_dependency_injection_can_attack():
  def randint(a, b): return 0
  assert_equal(main.make_a_move_with_dependency_injection(randint=randint), "Attack!")


def test_make_a_move_with_dependency_injection_can_defend():
  def randint(a, b): return 1
  assert_equal(main.make_a_move_with_dependency_injection(randint=randint), "Defend!")
