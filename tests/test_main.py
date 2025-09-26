from python_scaffolding.main import greetings


def test_greetings():
    """Test the greetings function returns hello world message."""
    result = greetings()
    assert result == "Hello, World!"
