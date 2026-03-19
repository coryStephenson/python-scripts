import requests

url_get = "http://httpbin.org/get"
payload = {"name":"Joseph","ID":"123"}
r_get = requests.get(url_get,params=payload)
r_get.url
r_get.request.body
r_get.status_code
r_get.text    # view the response as text
r_get.headers['Content-Type']     # view the MIME type a.k.a media type a.k.a content type
r_get.json()    # For content that's in JSON format, we format it using the json() method, returning the content as a python dict
r_get.json()['args'] # View the name and values for the query string


# The following endpoint will expect data, and it is a convenient way to configure an HTTP request to send data to a server
url_post = "http://httpbin.org/post"

# The payload dictionary
payload = {"name":"Joseph","ID":"123"}

# To make a POST, we use the POST function; the variable payload is passed to the parameter data.
r_post = requests.post(url_post,data=payload)

print("POST request URL: ",r_post.url)
print("GET request URL: ",r_get.url)

print("POST request body: ",r_post.request.body)
print("GET request body: ",r_get.request.body)

r_post.json()['form'] # View the payload




