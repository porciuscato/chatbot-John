from flask import Flask, render_template, request
from faker import Faker
import random
import requests
from bs4 import BeautifulSoup
fake = Faker('ko_KR')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')


names = {}

@app.route('/result')
def result():
    name = request.args.get('name')
    
    # 1. names에 해당하는 이름이 있는지 없는지 확인
    if name in names:
    # 2. 있다면 => names에 저장된 직업을 보여줌
        job = names[name]
    else:
        job = fake.job()
        names[name] = job
    # 3. 없다면 => 랜덤으로 fake 직업을 보여줌, names에 저장

    return render_template('result.html', job=job, name=name)

@app.route("/goonghap")
def goonghap():
    return render_template('goonghap.html')

babos = {}

@app.route('/destiny')
def destiny():
    babo = request.args.get('babo')
    you = request.args.get('you')

    # 1. 이름 + 이름으로 저장
    # if babo + you in babos:
    #     percent = babos[babo + you] 
    # else:
    #     percent = random.randint(51, 101)
    #     babos[babo + you] = percent

    # 2. dict in dict
    if babo in babos:
        if you in babos[babo]:
            percent = babos[babo][you]
        else:
            percent = random.randint(51, 101)
            babos[babo][you] = percent
    else:
        percent = random.randint(51, 101)
        babos[babo] = {you: percent}
    
    return render_template('destiny.html', babo=babo, you=you, percent=percent)

# babos 있는 사람들을 모두 출력하기
@app.route('/admin')
def admin():
    # babos dictionary에 있는 모든 데이터를 admin.html에 출력

    return render_template('admin.html', babos=babos)


@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/search')
def sresult():
    username = request.args.get("username")

    # 1. op.gg에 요청을 보낸다.
    url = "https://www.op.gg/summoner/userName=" + username

    # 2. html 응답을 받아
    res = requests.get(url)

    # 3. html 안에 있는 정보를 출력 (bs4)
    doc = BeautifulSoup(res.text, "html.parser")
    win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins').text
    loss = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.loses').text

    return render_template('search.html', win=win, loss=loss)

if __name__ == '__main__':
    app.run(debug=True)