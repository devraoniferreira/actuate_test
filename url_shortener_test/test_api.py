import requests

BASE_URL = "http://localhost:8000"

def test_create_short_url():
    """Tests creating a shortened URL."""
    response = requests.post(f"{BASE_URL}/short/", json={"url": "https://www.google.com"})
    assert response.status_code == 200, f"Error shortening URL: {response.text}"
    short_url = response.json().get("short_url")
    assert short_url, "short_url was not returned correctly"
    return short_url

def test_duplicate_url():
    """Tests whether the same URL generates the same short_url."""
    response1 = requests.post(f"{BASE_URL}/short/", json={"url": "https://www.google.com"})
    response2 = requests.post(f"{BASE_URL}/short/", json={"url": "https://www.google.com"})
    assert response1.json().get("short_url") == response2.json().get("short_url"), "Duplicate URLs returned different short_urls"

def test_invalid_url():
    """Tests whether an invalid URL returns a 400 error."""
    response = requests.post(f"{BASE_URL}/short/", json={"url": "not_a_valid_url"})
    assert response.status_code == 400, f"Expected 400, received {response.status_code}"

def test_get_original_url():
    """Tests retrieving the original URL from a short_url."""
    short_url = test_create_short_url()
    response = requests.post(f"{BASE_URL}/long/", json={"short_url": short_url})
    assert response.status_code == 200, f"Error retrieving original URL: {response.text}"
    assert response.json().get("url") == "https://www.google.com", "Original URL does not match"

def test_invalid_short_url():
    """Tests querying an invalid short_url."""
    response = requests.post(f"{BASE_URL}/long/", json={"short_url": "invalid123"})
    assert response.status_code == 404, f"Expected 404, received {response.status_code}"

def test_redirect():
    """Tests redirecting from short_url to original URL."""
    short_url = test_create_short_url()
    response = requests.get(f"{BASE_URL}/{short_url}", allow_redirects=False)
    assert response.status_code == 307, f"Expected 307, received {response.status_code}"
    assert response.headers["location"] == "https://www.google.com", "Incorrect redirection"

def test_invalid_redirect():
    """Tests redirecting with an invalid short_url."""
    response = requests.get(f"{BASE_URL}/invalid123", allow_redirects=False)
    assert response.status_code == 404, f"Expected 404, received {response.status_code}"

def test_access_count():
    """Tests counting accesses to the short_url."""
    short_url = test_create_short_url()
    requests.get(f"{BASE_URL}/{short_url}")  # Simulate an access
    response = requests.get(f"{BASE_URL}/count/{short_url}")
    assert response.status_code == 200, f"Error retrieving access count: {response.text}"
    assert response.json().get("click_count") == 1, f"Expected 1 access, received {response.json().get('click_count')}"

def test_invalid_access_count():
    """Tests counting accesses for an invalid short_url."""
    response = requests.get(f"{BASE_URL}/count/invalid123")
    assert response.status_code == 404, f"Expected 404, received {response.status_code}"

if __name__ == "__main__":
    test_create_short_url()
    test_duplicate_url()
    test_invalid_url()
    test_get_original_url()
    test_invalid_short_url()
    test_redirect()
    test_invalid_redirect()
    test_access_count()
    test_invalid_access_count()
    print("All tests passed!")