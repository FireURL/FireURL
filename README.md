# FireURL (v.0.2)
Open url from a POST request. Simple Python script that fires a URL from a POST request to the server computer.

## Requirements
- Python 2.x
- Computer running Linux, Windows, Mac with any browsers

### How to use
Start fireURL with one of the followings:

```bash
python firURL.py # Will start fireURL on default port 8000
```

or

```bash
python fireURL.py 6073  # Will start fireURL on port 6073.
```

Send a POST request to the running server. Using ```curl``` in this example.
```bash
curl --data "url=https://google.com" 192.168.1.x.x:8000
```

If you are not using ```curl```, make sure you format the data-form as followings:
```json
{
  "url": "https://google.com"
}
```

The protocol of the URL can be omitted, ```fireURL``` will automatically prepend ```http://``` in front. For example:

```json
{
  "url": "google.com"
}
```
will automatically be interpreted as ```url="http://google.com"```.

Server computer will now show up a new browser window. Enjoy!
