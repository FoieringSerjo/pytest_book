import random


def test_1_pass():
  ...


def test_2_always_fail():
  assert False, "always fail"


def test_3_pass():
  ...


def test_4_random_failure():
  outcome = random.choice([True, False])
  assert outcome, "random failure"


def test_5_pass():
  ...
