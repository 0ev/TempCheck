import requests

import requests

cookies1 = {
    '_ga': 'GA1.3.652922985.1613313402',
    '_gid': 'GA1.3.1553330226.1613979425',
    '__RequestVerificationToken': 'baBC-8xdnkZdsnzxeRhsrSoV01N1EjTVl7SfOVgelpiy0Zfb3xPfxoP7zq3LiOqxKl-cYo7DPl7lfp-NoMqh0Rh6yn0XZ31rwcJlkutSbZU1',
    'ASP.NET_SessionId': 'c0x1h2vcrbjttav3m0pndpxs',
    '_gat': '1',
}

cookies2 = {
    '_ga': 'GA1.3.652922985.1613313402',
    '_gid': 'GA1.3.1553330226.1613979425',
    '__RequestVerificationToken': 'baBC-8xdnkZdsnzxeRhsrSoV01N1EjTVl7SfOVgelpiy0Zfb3xPfxoP7zq3LiOqxKl-cYo7DPl7lfp-NoMqh0Rh6yn0XZ31rwcJlkutSbZU1',
    'ASP.NET_SessionId': 'c0x1h2vcrbjttav3m0pndpxs',
    '.AspNet.ApplicationCookie': 'lpM6IhrMqvti2ejxer9aA2BAb0xxRsPhv-oHfHvAkMvPHd9jQsTatMGrzl4M7mEJapX4VhROnWj6jIBrfNqUYkeP63AFmirr131ZkVCy_5AQUp-gkw_YZtOxDh6KYH8BzLJ4cZ5_iYCF-WaW9ASuXcVKSwm3v6GjlkvRBdjphYcy97LM8ERVOdeRe5TnAcvXU_dcrJUPBIAXLx_I6c8titx3Bqh6DwZUrnm7NT7Vwkc_B-3jAyFagj3tEjtQbVKRkOEMRZyaU0-arNi9Xzu640H76-XjvKYoFJrPhehckLy1vr0PxjWqzQYMzQD6ICUqLfiBANAHvf7ZQEo1-ZY9vf6O9KxlRR20F5gnIEVuGel0dsUJLPZbjNDWAxvDgXa9bCeXatN6vj5T20FHu2gd-KgrvJnMWPsM1gCWjXnaZWh1H19aARi7H0dEuH4SOS8zP8OLi6B2GcKpSBZLoAAvByHH473ZMUH1bHp1cSBW2-ZG9swFrgBxACcdkcYNJzKGPkwG3SGDIQ_PnYXnYHCtA2Io7dgXxLjSq7qvlMN2188',
    '_gat': '1',
}


headers1 = {
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

data1 = '''-----------------------------59360927115278807333697851719
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

headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

data3 = {
  '__RequestVerificationToken': 'ilVc4I8me_uQOEEK70dkfTb7xU5ffjOIbSyYJnCKE3ZXNUK7w5UPz3bDtsmZDOVbhjgKOdnI2WGa3_AkFnpvBs52zdTImwGs-ruggWX0laaD2xZh1NVnwK4f08Rr886gnFdxRqFnq5c_ZGWHJhP9Fw2',
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

headers3 = {
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


with requests.Session() as s:

    response = requests.post('https://www.ksa.hs.kr/Account/Login', data = data1.encode("utf-8"), headers=headers1, cookies=cookies1)

    # print(response.text)

    response = requests.get('https://www.ksa.hs.kr/SelfHealthCheck/Symptom', headers=headers2, cookies=cookies2)

    print(response.text)



    response = requests.post('https://www.ksa.hs.kr/SelfHealthCheck/Update', headers=headers2, cookies=cookies2, data=data3)

    print(response.text)


import requests

cookies = {
    '_ga': 'GA1.3.652922985.1613313402',
    '_gid': 'GA1.3.1553330226.1613979425',
    '__RequestVerificationToken': 'baBC-8xdnkZdsnzxeRhsrSoV01N1EjTVl7SfOVgelpiy0Zfb3xPfxoP7zq3LiOqxKl-cYo7DPl7lfp-NoMqh0Rh6yn0XZ31rwcJlkutSbZU1',
    'ASP.NET_SessionId': 'c0x1h2vcrbjttav3m0pndpxs',
    '_gat': '1',
    '.AspNet.ApplicationCookie': '_vYGSd0s2ZTdLmUryCs7mAoqkVqdWG9Oh24U8S-_UH1ydwwmkn3tl8chVYxp_-r5xz7siqyH0Zmetz7qF2yb-pXC2BwOVuDhW63TXWojUx-UesuFEWXg1gzQUpqxH7SUqfXK8s7V5Tw-4DViT4FLi4O2ulFMYDxU5OdkQaxrrRVQgUp0chgZ0wtjRBGp9IAvFoUA3H3HjdK28lWzlg1-7Am4IY_V8BunjkchI9HMg64tuQqK1HfyNoOPdg_oAQXh6u0fiO0oRlpAWRssPaxr-XPI0Syr4_w8AOwKCOg4c-piKN3iEs0pn_c90dXQcNqZjkE-GXEnMNKIMnTNomrJEISMDLsjDesXzaw3ekC2oVjFigP9Depk_cRuaAAetL2JdCISI61g51UyvmWT9XNxE12AcAVNyysnO8-lrrj3tjhzxSZfruresThD2umfIQhOs2B2SKYdbmLB1zqj9xJu8z7joxe_q01EiKGqWW0JMtkSGc-2UZZKI2q7ezRj7Sumv9HlM3DavgmDzJ8ZhZeAiNk8GuJSqrS18Vn8aWR3Zc4',
}

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

data = {
  '__RequestVerificationToken': 'ilVc4I8me_uQOEEK70dkfTb7xU5ffjOIbSyYJnCKE3ZXNUK7w5UPz3bDtsmZDOVbhjgKOdnI2WGa3_AkFnpvBs52zdTImwGs-ruggWX0laaD2xZh1NVnwK4f08Rr886gnFdxRqFnq5c_ZGWHJhP9Fw2',
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

response = requests.post('https://www.ksa.hs.kr/SelfHealthCheck/index/200', headers=headers, cookies=cookies, data=data)
