from unittest import mock

import cards
import pytest

from cards_cli_helper import cards_cli


@pytest.fixture()
def mock_cardsdb():
    with mock.patch.object(cards, "CardsDB") as CardsDB:
        yield CardsDB.return_value


def test_config(mock_cardsdb):
    mock_cardsdb.path.return_value = "/foo/"
    result = cards_cli("config")
    assert result == "/foo/"
