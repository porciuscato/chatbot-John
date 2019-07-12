from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint
app = Flask(__name__)

token = config('TELEGRAM_TOKEN')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    # chat_id를 가져오는 코드
    # 1. getUpdates 메소드로 요청 보내기

    base = "https://api.telegram.org"
    method = "getUpdates"

    url = f"{base}/{token}/{method}"
    res = requests.get(url).json()

    chat_id = res['result'][0]['message']['chat']['id']
    # 2. 받아온 응답(json)을 dictionary로 바꿔서 
    
    # 3. 첫번째 메세지의 chat_id를 가져온다.
    
    method = "sendMessage"
    # home에 보내온 msg를 받아 telegram api를 통해 메시지 전송
    text = request.args.get('msg')

    url = f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"

    requests.get(url)
    
    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])
def webhook():
    # 1. 메아리 챗봇
    # (1) webhook을 통해 telegram 보낸 요청 안에 있는 메세지를 가져와
    # (2) 그대로 전송
    res = request.get_json()
    text = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')


    base = "https://api.telegram.org"
    method = "sendMessage"

    url = f"{base}/bot{token}/{method}?chat_id={chat_id}&text={text}"
    requests.get(url)
    return '', 200

if __name__ == "__main__":
    app.run(debug=True)