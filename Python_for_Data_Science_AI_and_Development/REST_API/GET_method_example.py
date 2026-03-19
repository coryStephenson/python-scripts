import requests

url = 'https://www.ibm.com/'

r = requests.get(url)

r.status_code :200

r.request.headers

r.request.body:None

header = r.headers

header['date']

header['Content-Type']

r.encoding

r.text[0:100]  # review the first 100 characters


