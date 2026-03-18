import requests

def send_request(url):
    """Send a GET request to the specified URL and print the status code."""
    try:
        response = requests.get(url)
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(e)

url = "https://www.example.com"
send_request(url)
```

The issue was fixed by adding a docstring to the `send_request` function, which is a good practice in Python. This docstring explains what the function does, which makes the code more readable and maintainable.