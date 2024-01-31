from subprocess import run


def test_hello():
    result = run(["python", "hello.py"], capture_output=True, text=True)
    output = result.stdout
    assert output == "Hello, World!\n"


def test_hello_with_name():
    result = run(["python", "hello.py", "Brian"], capture_output=True, text=True)
    output = result.stdout
    assert output == "Hello, Brian!\n"
