import requests
import bs4

url = "https://finance.naver.com/sise/"

ex_url = "https://finance.naver.com/marketindex/"

response = requests.get(url).text

response_ex = requests.get(ex_url).text

document = bs4.BeautifulSoup(response, 'html.parser')

document_ex = bs4.BeautifulSoup(response_ex, 'html.parser')


kospi = document.select_one('#KOSPI_now').text

kosdaq = document.select_one('#KOSDAQ_now').text

ex = document_ex.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print('현재 코스피 지수는 : ' + kospi)

print('현재 코스닥 지수는 : ' + kosdaq)

print('현재 원/달러 환율은 : ' + ex)

