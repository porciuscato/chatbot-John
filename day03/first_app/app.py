from flask import Flask
# import flask
import random
from datetime import datetime
from bs4 import BeautifulSoup
app = Flask(__name__)

# 1. 주문 받는 방식(어떻게)
@app.route("/")
# 2. 무엇을 제공할지(무엇)
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "hi"

# 1. /name
# 2. 여러분의 영문이름

@app.route("/name")
def myname():
    return "john"

@app.route("/hello/<person>")
def hello2(person):
    # return "hello " + person
    return f"hello {person}"

# /cube/1 => 1
# /cube/2 => 8
# /cube/3 => 27
@app.route("/cube/<num>")
def cube(num):
    result = int(num) ** 3
    return str(result)

@app.route("/lotto")
def lotto():
    # 1. /lotto => 랜덤 로또 번호 추천 
    return str(sorted(random.sample(range(1, 46), 6)))

@app.route("/menu")
def menu():
    # 2. /menu => 점심 메뉴 추천
    menus = ["햄버거", "피자", "파스타"]
    return str(random.choice(menus))
    # return 

# 3. /kospi => 현재 네이버 기준 kospi
# bs4.BeautifulSoup

# /newyear
@app.route("/newyear")
def newyear():
    month = datetime.now().month
    day = datetime.now().day
    # 만약 오늘이 1월 1일 이라면,
    if month == 1 and day == 1:
        print("이건 프린트")
        return "<h1>예</h1>"
    else:
        return "<h1>아니요</h1>"

# /index
@app.route("/index")
def index():
    return "<html><head></head><body><h1>홈페이지</h1><p>이건내용</p></body></html>"