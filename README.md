# FireURL (v.0.3)
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

### Via POST request
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



### Via GET request
Starting from version 0.3, GET requests will also be supported. Usage as following:

URL format:
```
GET http://SERVER_ADDR:PORT/?url=URL_TO_BE_FIRED
```

Example using curl:
```bash
curl http://192.168.x.x/?url=http://facebook.com
```

### Format of url
The protocol of the URL can be omitted, ```fireURL``` will automatically prepend ```http://``` in front. For example:

```json
{
  "url": "google.com"
}
```
will automatically be interpreted as ```url="http://google.com"```.

Server computer will now show up a new browser window. Enjoy!
