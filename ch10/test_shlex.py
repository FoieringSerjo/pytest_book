import shlex


def test_shlex():
    assert shlex.split("version") == ["version"]
    assert shlex.split("list -o brian") == ["list", "-o", "brian"]
