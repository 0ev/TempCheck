from flask import Flask
from flask.wrappers import Request
from run import run

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def api():
    return "어케옴?"

@app.route('/api', methods = ['POST'])
def test():
    data = request.get_json()

    id = data["id"]
    password = data["password"]

    try:
        result = run(id,password)

        if result["result"] == -1:
            return "벌써 체온체크를 하였습니다"
        if result["result"] == 1:
            return "성공하였습니다"

    except:
        return "비밀번호나 아이디가 잘못되었습니다 다시 시도해주세요"
    
@app.route('/test/<data>', methods = ['GET'])
def test2(data):

    id = data.split("|")[0]
    password = data.split("|")[1]

    try:
        result = run(id,password)
        
        if result["result"] == -1:
            return "벌써 체온체크를 하였습니다"
        if result["result"] == 1:
            return "성공하였습니다"

    except:
        return "비밀번호나 아이디가 잘못되었습니다 다시 시도해주세요"

if __name__ == '__main__':
    app.run()