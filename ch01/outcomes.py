import pytest


def test_passing():
    assert 1 == 1


def test_failing():
    assert 1 == 2


@pytest.mark.skip(reason="example of skip")
def test_skipped():
    ...


@pytest.mark.xfail(reason="example of xfail")
def test_xfail():
    assert 1 == 2


@pytest.mark.xfail(reason="example of xpass")
def test_xpass():
    assert 1 == 1


@pytest.fixture()
def some_fixture():
    assert 1 == 2


def test_error(some_fixture):
    ...