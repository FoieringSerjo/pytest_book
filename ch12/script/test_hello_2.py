import shlex
from subprocess import run


def test_hello():
    command = shlex.split("python hello.py")
    result = run(command, capture_output=True, text=True)
    output = result.stdout
    assert output == "Hello, World!\n"


def test_hello_with_name():
    command = shlex.split("python hello.py Brian")
    result = run(command, capture_output=True, text=True)
    output = result.stdout
    assert output == "Hello, Brian!\n"
