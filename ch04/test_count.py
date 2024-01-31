import cards


def test_empty(cards_db):
    print("test_empty()")
    assert cards_db.count() == 0


def test_two(cards_db):
    print("test_two()")
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2
