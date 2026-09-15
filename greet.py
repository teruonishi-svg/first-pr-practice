def greet(name):
    """Return a friendly greeting for name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys
    who = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(who))
