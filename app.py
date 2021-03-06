from flask import Flask, request, render_template, redirect,url_for,abort

import game
import json

app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html',data=character)

@app.route('/senddata') 
def senddata(): 
    name = 'world' 
    return render_template('senddata.html', data=name)


@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['items'])
    return "{} 이 {}아이템을 사용 해서 이겼다.".format(character["name"], character["items"][0])

@app.route('/input/<int:num>')
def input_num(num):
    if num ==1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character=json.loads(data)
            print(character['items'])
        return "{} 이 {}아이템을 사용 해서 이겼다.".format(character["name"], character["items"][0])
    elif num ==2:
        return "도망갔다."
    elif num ==3:
        return "퉁퉁이"
    else:
        return "없어요"

    
#로그인
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        # id와 pw가 임의로 정한 값이랑 비교 해서 맞으면 맞다 틀리면 틀리다
        if id == 'abc' and pw == '1234':
            return "안녕하세요 {} 님".format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."


@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'GET':
        return 'GET 입니다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        with open("static/save.txt","w", encoding='utf-8') as f:
            f.write("%s,%s" % (num, name))
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num,name)


@app.route('/getinfo')
def getinfo(): 
# 파일 입력 
    with open("static/save.txt", "r", encoding='utf-8') as file: 
        student = file.read().split(',') # 쉽표로 잘라서 student 에 배열로 저장 
        return '번호 : {}, 이름 : {}'.format(student[0], student[1])



@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")

@app.route('/kakao')
def daum():
    return redirect("https://www.daum.net/")

@app.route('/url_test')
def url_test():
    return redirect(url_for('naver'))

@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'daum':
        return redirect(url_for('daum'))
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. url을 확인 하세요",404

@app.route('/img')
def img():
 return render_template("image.html")

if __name__ == '__main__':
    app.run(debug=True)
