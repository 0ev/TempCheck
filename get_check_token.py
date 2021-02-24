import requests
from get_login_token import get_login_token
from initialize import initialize
from login import login
from bs4 import BeautifulSoup

def get_check_token(token):

    cookies = {
        '_ga': 'GA1.3.652922985.1613313402',
        '_gid': 'GA1.3.1553330226.1613979425',
        '__RequestVerificationToken': token,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.ksa.hs.kr/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.get('https://www.ksa.hs.kr/SelfHealthCheck/Index/200', headers=headers, cookies=cookies)

    print(response.text)

    # print(response.headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.find_all('input', {"name":"__RequestVerificationToken"}))

    result = soup.find_all('input', {"name":"__RequestVerificationToken"})[-1]["value"]

    print("check_token : " + result)

    return result