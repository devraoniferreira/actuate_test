from src.payload import ShortRequest

def test_dummy():
    assert 1 == 1

def test_short():
    short_request = ShortRequest(url="https://www.google.com")
    assert short_request.url == "https://www.google.com"
