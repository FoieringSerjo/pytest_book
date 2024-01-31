import shlex
from subprocess import run

import pytest


@pytest.mark.parametrize(
    "command, expected",
    [
        ("python hello.py", "Hello, World!"),
        ("python hello.py Brian", "Hello, Brian!"),
    ],
)
def test_hello(command, expected):
    result = run(shlex.split(command), capture_output=True, text=True)
    output = result.stdout.rstrip()
    assert output == expected
