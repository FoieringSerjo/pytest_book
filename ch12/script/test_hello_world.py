from subprocess import run


def test_hello():
    result = run(["python", "hello_world.py"], capture_output=True, text=True)
    output = result.stdout
    assert output == "Hello, World!\n"
