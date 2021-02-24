'''
requests。session 来保持状态。自动管理过程中产生的Cookie
下次请求时自动带上上一次的Cookie
'''

import requests

# requests.get()
s = requests.session()
print(s.cookies)
print("登录前的cookies：",requests.utils.dict_from_cookiejar(s.cookies))

# 登录接口
url = "https://www.bagevent.com/user/login"
cs = {

    # "account": "2780487875@qq.com ",
    # "password": "qq2780487875"
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": "1"
}
r = s.post(url,data=cs)
print("登录后的cookies：",requests.utils.dict_from_cookiejar(s.cookies))
# print(r.text)
assert "<title> 百格活动 - 账户总览</title>" in r.text

# dashboard接口
r= s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)

# 退出登录的接口
r = s.get("https://www.bagevent.com/user/login_out")
print("退出登录后的cookies：",requests.utils.dict_from_cookiejar(s.cookies))