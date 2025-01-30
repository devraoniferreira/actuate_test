import hashlib

db = {}
counter = {}


def generate_short_url(url: str) -> str:
    '''
        Generate a short URL for a given long URL.
        url: str: The long URL to shorten.
        return: str: The short URL.
    '''
    short_url = hashlib.md5(url.encode()).hexdigest()[:6] 
    db[short_url] = url
    return short_url

def retrieve_long_url(short_url: str) -> str:
    '''
        Retrieve the long URL for a given short URL.
        short_url: str: The short URL to retrieve.
        return: str: The long URL.
    '''
    return db.get(short_url, "")


def increment_click_count(short_url: str):
    '''
        Increment the click count for a given short URL.
        short_url: str: The short URL to increment the click count for.
        return: None
    '''
    counter[short_url] = counter.get(short_url, 0) + 1


def get_click_count(short_url: str) -> int:
    '''
        Get the click count for a given short URL.
        short_url: str: The short URL to get the click count for.
        return: int: The click count.
    '''
    return counter.get(short_url, 0)
