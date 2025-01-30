# Actuate URL Shortener

This project is a URL shortener. It has three functionalities: first, a shortener, where the user submits a URL and it's shortened; second, an endpoint to consult the original URL from a shortened URL; and finally, redirection from the shortened URL to the original website.


## Running

First make sure your system has python installed:

```bash
python -V
```

After this, run the following commands in the folder of the project:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn endpoint:app
```

The project will start running in your localhost in port 8000

[http://localhost:8000/](http://localhost:8000/)

## How to use

The project has 4 endpoints.

 1. POST /short/
    
The server receives the url, creates a short version and answers to the user this short version

*payload*:
 ```json
{
    "url": "https://www.google.com"
}
```
*example*:
```bash
curl --header "Content-Type: application/json" --request POST --data '{"url":"www.google.com"}' http://localhost:8000/short
```

 2. POST /long/

The server receives the shortened url and gives back the original URL 

*payload*:
 ```json
{
    "short_url": "0a137b"
}
```
*example*:
```bash
curl --header "Content-Type: application/json" --request POST --data '{"short_url":"0a137b"}' http://localhost:8000/long
```

 3. GET /{short_url}

Redirects from the short url to the original website


4. GET /count/{short_url}

Returns the number of times the short url was accessed


## Tests
There are some example tests in the project. To run them, use the following command:

```bash
python -m pytest
```

## Frontend
The application has a frontend, with the server running, access it using the following URL:

[http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)
