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
    assert cards_cli("config") == "/foo/"


def test_path(mock_cardsdb):
    mock_cardsdb.path.return_value = "/foo/"
    assert mock_cardsdb.path() == "/foo/"


def test_bad_mock(mock_cardsdb):
    mock_cardsdb.path(35)  # invalid arguments
    mock_cardsdb.not_valid()  # invalid function


@pytest.fixture()
def mock_cardsdb_with_autospec():
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDB:
        yield CardsDB.return_value


def test_autospec_mock(mock_cardsdb_with_autospec):
    mock_cardsdb_with_autospec.path(35)  # invalid arguments
    mock_cardsdb_with_autospec.not_valid()  # invalid function
