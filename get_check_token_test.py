import requests

cookies = {
    '_ga': 'GA1.3.652922985.1613313402',
    '_gid': 'GA1.3.1553330226.1613979425',
    '__RequestVerificationToken': 'KUX6SuG813Od962CvfxtTqU3u6EPHQESnMOQWzE8EyDv78e8v2lMRjeWl9_RHjkLYVoiX88JnOmlPdggI52akeY3K5bT_V3wBmCO2ZA_zG41',
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
