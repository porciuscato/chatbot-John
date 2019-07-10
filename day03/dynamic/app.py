from flask import Flask, render_template
import random
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/hello/<name>')
def hello(name):
    # name에는 /hello/이름/ 활용가능
    return render_template('hello.html', username=name)

@app.route('/menu')
def menu():
    # 1. 랜덤으로 음식 메뉴를 추천하고,
    menus = ["햄버거", "김밥", "떡볶이"]
    choice = random.choice(menus)
    
    images = {
        "햄버거": "http://img.hani.co.kr/imgdb/resize/2017/0709/149948783091_20170709.JPG",
        "김밥": "http://recipe1.ezmember.co.kr/cache/recipe/2016/06/29/e83ce1d994ff9b5ffcd1981c8971119d1.jpg",
        "떡볶이": "http://recipe1.ezmember.co.kr/cache/recipe/2015/06/22/deb8bf13462e06865665ca1b6f691f5a.jpg"
    }
    # 2. 해당 음식 사진을 보여주는 기능을 구현
    image = images[choice]

    return render_template('menus.html', name=choice, image=image)

@app.route('/lotto')
def lotto():
    # /lotto 랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능
    
    # 1. 1등 숫자를 가져오기
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    dict_lotto = res.json()
    winner = []
    for i in range(1, 7):
        winner.append(dict_lotto[f'drwtNo{i}'])
    # 2. 비교하기
    your_lotto = sorted(random.sample(range(1, 46), 6))
    count = len(set(winner) & set(your_lotto))

    # 3. 등수 알려주기
    if count == 6:
        grade = "1등"
    elif count == 5:
        grade = "3등"
    elif count == 4:
        grade = "4등"
    elif count == 3:
        grade = "5등"
    else:
        grade = "꽝"
    
    return render_template('lotto.html', winner=str(winner), lotto=str(your_lotto), grade=grade)


if __name__ == "__main__":
    app.run(debug=True)