import requests

cookies = {
    '_ga': "GA1.3.652922985.1613313402",
    '_gid': "GA1.3.7529032.1613313402",
    '__RequestVerificationToken': "y1l55l-X0aEpNgmw4tGKsFKKR1JbwtVTPooHDS5osefgK4Wihu8Pp86bTyrHmCOEqzucObmxnaZrPTUOOe8654HRJAtAZuyKDe1YLoid4PY1",
    '_gat': '1'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'multipart/form-data; boundary=---------------------------228067104239788287011042795517',
    'Origin': 'https://ksa.hs.kr',
    'Connection': 'keep-alive',
    'Referer': 'https://ksa.hs.kr/Account/Login',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

files = {
    "__RequestVerificationToken" : "73ec5WTe69aVu0W2X2ry-Y3mT0aDNW0cCZjp7sSfTZg4n708_WGtrkslop0FZM6AUYKGdQRlwXwoiJq0pr1uBXHvZzJJK_w188qAFz0GPek1",
    "UserId" : "10fsdf58",
    "Password" : "316sdfsdfsdf526",
    "UserType" : "학생"
}




response = requests.post('https://ksa.hs.kr/Account/Login',headers = headers, cookies=cookies, data = files)

print(response.text)