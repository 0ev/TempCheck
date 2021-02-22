import requests
from bs4 import BeautifulSoup
from initialize import initialize

def get_login_token(token):

    cookies = {
        '_ga': 'GA1.3.652922985.1613313402',
        '_gid': 'GA1.3.1553330226.1613979425',
        '__RequestVerificationToken': token,
        '_gat': '1'
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

    response = requests.get('https://www.ksa.hs.kr/Account/Login', headers=headers, cookies=cookies)

    # print(response.headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('input', {"name":"__RequestVerificationToken"})["value"]

    print("login_token : " + result)

    return result
