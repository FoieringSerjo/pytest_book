# try running this both or without -s
# -s or --capture=no turns off pytest output capture


def test_pass():
    result = something()
    print(f"{result=}")
    assert result == 2


def test_fail():
    result = something()
    print(f"{result=}")
    assert result == 1


def something():
    print("\nsetting a")
    a = 1
    print(f"{a=}")

    print("setting b")
    b = 1
    print(f"{b=}")
    return a + b
