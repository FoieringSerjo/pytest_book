from typer.testing import CliRunner
import cards


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()


def test_patch_home(monkeypatch, tmp_path):
    def fake_home():
        return tmp_path

    monkeypatch.setattr(cards.cli.pathlib.Path,
                        "home",
                        fake_home)

    full_cards_dir = tmp_path / "cards_db"
    print(full_cards_dir)
    assert run_cards("config") == str(full_cards_dir)
    assert run_cards("count") == "0"
