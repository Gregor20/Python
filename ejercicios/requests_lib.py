import requests

url = "https://quotes.toscrape.com/"

request = requests.get(url)

print(request)

print(request.status_code)      # 'status_code' devuelve, el codigo http de vuelta (200 = ok)

print(request.content)          # 'content' devuelve el codigo html de la página web