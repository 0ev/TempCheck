from get_check_token import get_check_token
from get_login_token import get_login_token
from initialize import initialize
from login import login
from check import check
import requests

def run(id,password):

    with requests.Session() as s:
        initialize(s)
        login_token = get_login_token(s)
        login(s,login_token,id,password)
        check_token = get_check_token(s)
        check(s, check_token, True)

run("id","password")