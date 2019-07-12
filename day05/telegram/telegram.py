import requests
from pprint import pprint
from decouple import config

base = "https://api.telegram.org"
token = config('TELEGRAM_TOKEN')
print(token)
method = "getUpdates"

url = f"{base}/{token}/{method}"
res = requests.get(url).json()

pprint(res)

# chat_id = "224026642"
# text = "하이하이"
# url = f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"

# res = requests.get(url)
# print(res.text)