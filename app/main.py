#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from flask import Flask
from flask.wrappers import Request

app = Flask(__name__)

global USER_AGENT
global BASE_URL
global BASE_URL2
global LOGIN_URL
global TEMPCHECK_URL

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
BASE_URL = 'https://www.ksa.hs.kr'
BASE_URL2 = 'https://www.ksa.hs.kr/'
LOGIN_URL = 'https://ksa.hs.kr/Account/Login'
TEMPCHECK_URL = 'https://www.ksa.hs.kr/SelfHealthCheck/Index/200'


def initialize(s):

    headers = {
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
    }

    response = s.get(LOGIN_URL, headers=headers)


def get_login_token(s):

    headers = {
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Referer': BASE_URL2,
    }

    response = s.get('https://www.ksa.hs.kr/Account/Login', headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find_all(
        'input', {"name": "__RequestVerificationToken"})[-1]["value"]

    return result


def make_data(login_token, id, password):
    return f'''-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="__RequestVerificationToken"

{login_token}
-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="UserId"

{str(id)}
-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="Password"

{str(password)}
-----------------------------325333128821718686562724141506
Content-Disposition: form-data; name="UserType"

학생
-----------------------------325333128821718686562724141506--
'''


def login(s, login_token, id, password):

    headers = {
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'multipart/form-data; boundary=---------------------------325333128821718686562724141506',
        'Origin': 'https://ksa.hs.kr',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'Referer': LOGIN_URL,
    }

    response = s.post(LOGIN_URL, data=make_data(
        login_token, id, password).encode("utf-8"), headers=headers)


def get_check_token(s):

    headers = {
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Referer': BASE_URL2,
    }

    response = s.get(
        TEMPCHECK_URL, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find_all(
        'input', {"name": "__RequestVerificationToken"})[-1]["value"]

    return result


def check(s, check_token, has_symtom):
    # True:sick / False: normal
    data = {
        '__RequestVerificationToken': check_token,
        'survey_q1': str(has_symtom[0]),
        'survey_q2': str(has_symtom[1]),
        'survey_q3': str(has_symtom[2]),
        'SelfCheckItemDatas[0].Order': '1',
        'SelfCheckItemDatas[1].Order': '2',
        'SelfCheckItemDatas[2].Order': '3',
        'SelfCheckItemDatas[0].CheckResultValues[0]': '1' if has_symtom[0] else '0',
        'SelfCheckItemDatas[1].CheckResultValues[0]': '1' if has_symtom[0] else '0',
        'SelfCheckItemDatas[2].CheckResultValues[0]': '1' if has_symtom[0] else '0'
    }

    headers = {
        'User-Agent': USER_AGENT,
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': BASE_URL,
        'Connection': 'keep-alive',
        'Referer': TEMPCHECK_URL,
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    
    response = s.post(TEMPCHECK_URL, headers=headers, data=data)
    return response.json()


def run(id, password):
    with requests.Session() as s:
        initialize(s)
        login_token = get_login_token(s)
        login(s, login_token, id, password)
        check_token = get_check_token(s)
        result = check(s, check_token, True)
    return result


@app.route('/', methods=['POST', 'GET'])
def api():
    return "어케옴?".encode("utf-8")


@app.route('/api', methods=['POST'])
def test():
    data = request.get_json()
    user_id = data["id"]
    user_pw = data["password"]

    tryTempCheck(user_id, user_pw)


@app.route('/test/<data>', methods=['GET'])
def test2(data):
    user_id = data.split("|")[0]
    user_pw = data.split("|")[1]

    tryTempCheck(user_id, user_pw)


def tryTempCheck(user_id, user_pw):
    MSG_ALREADY = "이미 체온체크를 하셨습니다"
    MSG_SUCCESS = "성공하셨습니다"
    MSG_ERROR = "비밀번호나 아이디가 잘못되었으니 다시 시도해주세요"
    MSG_UNKNOWN = "예상치 못한 상황입니다"
    try:
        result = run(user_id, user_pw)
        if result["result"] == -1:
            return MSG_ALREADY.encode("utf-8")
        elif result["result"] == 1:
            return MSG_SUCCESS.encode("utf-8")
        else:
            return MSG_SUCCESS.encode("utf-8")
    except Exception:
        return MSG_ERROR.encode("utf-8")


if __name__ == '__main__':
    app.run()
