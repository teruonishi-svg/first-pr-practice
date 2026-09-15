from greet import greet


def test_greet_uses_name():
    assert greet("Teru") == "Hello, Teru!"


def test_greet_uses_world_by_default():
    assert greet("world") == "Hello, world!"
