"""
Test Cases for done
"""



def test_done(db_filled, known_set):
    """
    Should get cards 2 and 5 back:
        Card(summary="two", owner="Brian", state="done"),
        Card(summary="five", owner="Okken", state="done"),
    """
    result = db_filled.list_done_cards()
    assert len(result) == 2
    for i in (2, 5):
        assert known_set[i] in result

