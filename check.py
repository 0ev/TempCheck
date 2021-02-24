from get_check_token import get_check_token
from get_login_token import get_login_token
from initialize import initialize
from login import login
import requests

def check(s,check_token,okay):

    okay_data = {
    '__RequestVerificationToken': check_token,
    'SelfCheckItemDatas[0].Order': '1',
    'SelfCheckItemDatas[1].Order': '2',
    'SelfCheckItemDatas[2].Order': '3',
    'survey_q1': 'False',
    'SelfCheckItemDatas[0].CheckResultValues[0]': '0',
    'survey_q2': 'False',
    'SelfCheckItemDatas[1].CheckResultValues[0]': '0',
    'survey_q3': 'False',
    'SelfCheckItemDatas[2].CheckResultValues[0]': '0'
    }

    not_okay_data = {
    '__RequestVerificationToken': check_token,
    'SelfCheckItemDatas[0].Order': '1',
    'SelfCheckItemDatas[1].Order': '2',
    'SelfCheckItemDatas[2].Order': '3',
    'survey_q1': 'True',
    'SelfCheckItemDatas[0].CheckResultValues[0]': '1',
    'survey_q2': 'True',
    'SelfCheckItemDatas[1].CheckResultValues[0]': '1',
    'survey_q3': 'True',
    'SelfCheckItemDatas[2].CheckResultValues[0]': '1'
    }

    if okay:
        data = okay_data
    elif not okay:
        data = not_okay_data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.ksa.hs.kr',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ksa.hs.kr/SelfHealthCheck/Index/200',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = s.post('https://www.ksa.hs.kr/SelfHealthCheck/index/200', headers=headers, data=data)
    print(response.text)


