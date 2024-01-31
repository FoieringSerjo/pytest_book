from cards import Card


def test_finish(cards_db):
    for c in [
        Card("write pytest book", state="done"),
        Card("create video course", state="in prog"),
        Card("write tdd book", state="todo"),
    ]:
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"
