from flask import Flask, render_template, request
from faker import Faker
fake = Faker('ko_KR')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pastlife')
def pastlife():
    return render_template('pastlife.html')

@app.route('/result')
def result():
    name = request.args.get('name')
    names = {}

    # 1. 우리 names에 해당하는 이름이 있는지 없는지 확인

    # 2. 없다면 => 랜덤으로 fake 직업을 보여줌, names에 저장

    # 3. 있다면 => names에 저장된 직업을 보여줌


    return render_template('result.html', job=job, name=name)

if __name__ == '__main__':
    app.run(debug=True)