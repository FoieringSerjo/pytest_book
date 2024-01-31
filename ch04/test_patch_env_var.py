from typer.testing import CliRunner
import cards


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_patch_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))

    assert run_cards("config") == str(tmp_path)
    assert run_cards("count") == "0"

