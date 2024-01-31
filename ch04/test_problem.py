from typer.testing import CliRunner
import cards


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()



def test_count_while_empty():
    output = run_cards("count")
    assert output == '0'


def test_debug_list(capsys):
    output = run_cards("list")
    with capsys.disabled():
        print(output)


def test_debug_config(capsys):
    output = run_cards("config")
    with capsys.disabled():
        print(output)
