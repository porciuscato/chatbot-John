# lotto api를 통해 최신 당첨번호를 가져온다.
import requests
import random

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
res = requests.get(url)
dict_lotto = res.json()

winner = []

for i in range(1, 7):
    winner.append(dict_lotto[f'drwtNo{i}'])

if count == 6:
    print("1등")
elif count == 5:
    print("3등")
elif count == 4:
    print("4등")
elif count == 3:
    print("5등")
else:
    print("꽝")

trial = 0

while True:
    your_lotto = sorted(random.sample(range(1, 46), 6))
    count = len(set(winner) & set(your_lotto))

    if count == 6:
        print("1등입니다.")
        break

    trial += 1
    print(trial)