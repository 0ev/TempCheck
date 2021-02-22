from get_check_token import get_check_token
from get_login_token import get_login_token
from initialize import initialize
from login import login
from check import check

token = initialize()
login_token = get_login_token(token)
login(token,login_token)
check_token = get_check_token(token)
check(token, check_token, True)