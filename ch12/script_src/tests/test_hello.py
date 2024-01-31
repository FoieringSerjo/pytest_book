import hello


def test_hello(capsys):
    hello.main([])
    output = capsys.readouterr().out.rstrip()
    assert output == "Hello, World!"


def test_hello_brian(capsys):
    hello.main(["Brian"])
    output = capsys.readouterr().out.rstrip()
    assert output == "Hello, Brian!"


def test_parse_args_no_args():
    arg_n = hello.parse_args([])
    assert arg_n.name == "World"


def test_parse_args_Brian():
    arg_n = hello.parse_args(["Brian"])
    assert arg_n.name == "Brian"