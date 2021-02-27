from flask import Flask
from flask.wrappers import Request
from run import run

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def api():
    st = "어케옴?"
    st = st.encode("utf-8")
    return st

@app.route('/api', methods = ['POST'])
def test():
    data = request.get_json()

    id = data["id"]
    password = data["password"]

    try:
        result = run(id,password)

        if result["result"] == -1:
            st = "벌써 체온체크를 하였습니다"
            st = st.encode("utf-8")
            return st
        if result["result"] == 1:
            st = "성공하였습니다"
            st = st.encode("utf-8")
            return st

    except:
        st = "비밀번호나 아이디가 잘못되었습니다 다시 시도해주세요"
        st = st.encode("utf-8")
        return st
    
@app.route('/test/<data>', methods = ['GET'])
def test2(data):

    id = data.split("|")[0]
    password = data.split("|")[1]

    try:
        result = run(id,password)
        
        if result["result"] == -1:
            st = "벌써 체온체크를 하였습니다"
            st = st.encode("utf-8")
            return st
        if result["result"] == 1:
            st = "성공하였습니다"
            st = st.encode("utf-8")
            return st

    except:
        st = "비밀번호나 아이디가 잘못되었습니다 다시 시도해주세요"
        st = st.encode("utf-8")
        return st

if __name__ == '__main__':
    app.run()