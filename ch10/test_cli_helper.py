from cards_cli_helper import cards_cli


def test_cards_cli():
    result = cards_cli("version")
    print()
    print(f"version: {result}")

    result = cards_cli("list -o brian")
    print(f"list: {result}")


def test_version():
    result = cards_cli("version")
    assert result == "1.0.0"
