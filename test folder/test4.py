import requests

cookies = {
    '_ga': 'GA1.3.652922985.1613313402',
    '_gid': 'GA1.3.1553330226.1613979425',
    '__RequestVerificationToken': 'baBC-8xdnkZdsnzxeRhsrSoV01N1EjTVl7SfOVgelpiy0Zfb3xPfxoP7zq3LiOqxKl-cYo7DPl7lfp-NoMqh0Rh6yn0XZ31rwcJlkutSbZU1',
    'ASP.NET_SessionId': 'c0x1h2vcrbjttav3m0pndpxs',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'multipart/form-data; boundary=---------------------------59360927115278807333697851719',
    'Origin': 'https://www.ksa.hs.kr',
    'Connection': 'keep-alive',
    'Referer': 'https://www.ksa.hs.kr/Account/Login',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

data = '''-----------------------------59360927115278807333697851719
Content-Disposition: form-data; name="__RequestVerificationToken"

bGcW4gjfqun3xSUYwUEjin7fLa6_CAy1DTVSwKkbzrg_26cYoPKGLuCow8cSIw3peuOXDx_bEHWQpwYQqaLjew7DxorAmctCfhpD_mR4gT01
-----------------------------59360927115278807333697851719
Content-Disposition: form-data; name="UserId"

19-058
-----------------------------59360927115278807333697851719
Content-Disposition: form-data; name="Password"

3165626
-----------------------------59360927115278807333697851719
Content-Disposition: form-data; name="UserType"

학생
-----------------------------59360927115278807333697851719--
'''

response = requests.post('https://www.ksa.hs.kr/Account/Login', data = data.encode("utf-8"), headers=headers, cookies=cookies)

print(response.text)



