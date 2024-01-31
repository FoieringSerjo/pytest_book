import pytest
from cards import Card


@pytest.fixture(scope="function")
def cards_db_three_cards(cards_db):
    # add three cards
    cards_db.add_card(Card("Learn something new"))
    cards_db.add_card(Card("Build useful tools"))
    cards_db.add_card(Card("Teach others"))
    return cards_db


def test_zero_card(cards_db):
    assert cards_db.count() == 0


def test_three_card(cards_db_three_cards):
    cards_db = cards_db_three_cards
    assert cards_db.count() == 3
