import hello
from click.testing import CliRunner

runner = CliRunner()


def test_hello():
    result = runner.invoke(hello.main)
    assert result.stdout.rstrip() == "Hello, World!"


def test_hello_with_name():
    result = runner.invoke(hello.main, ["Brian"])
    assert result.stdout.rstrip() == "Hello, Brian!"
