import pytest
from cards import Card


@pytest.fixture(scope="module")
def known_set():
    # summary matches index into this list
    return [
        Card(summary="zero", owner="Brian", state="todo"),
        Card(summary="one", owner="Brian", state="in prog"),
        Card(summary="two", owner="Brian", state="done"),
        Card(summary="three", owner="Okken", state="todo"),
        Card(summary="four", owner="Okken", state="in prog"),
        Card(summary="five", owner="Okken", state="done"),
    ]


@pytest.fixture(scope="module")
def db_filled(session_cards_db, known_set):
    cards_db = session_cards_db

    # make sure it's empty
    cards_db.delete_all()

    # then add our known set
    for c in known_set:
        cards_db.add_card(c)
    return cards_db