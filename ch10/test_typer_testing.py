from cards.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_typer_runner():
    result = runner.invoke(app, ["version"])
    print()
    print(f"version: {result.stdout}")

    result = runner.invoke(app, ["list", "-o", "brian"])
    print(f"list: {result.stdout}")


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.stdout.rstrip() == "1.0.0"
