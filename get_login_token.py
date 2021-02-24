import requests
from bs4 import BeautifulSoup
from initialize import initialize

def get_login_token(s):

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

    response = s.get('https://www.ksa.hs.kr/Account/Login', headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find_all('input', {"name":"__RequestVerificationToken"})[-1]["value"]

    return result
    