import  requests

# 表单格式的数据：content-type:www-x-from-urlencoded,使用data传参
# 登录接口
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {
    "mobilephone": "15129938628",
    "pwd":"123456"
}
r = requests.post(url, data=cs)
print(r.text)
rjson = r.json()
assert rjson['status'] == 1
assert rjson['code'] == '10001'

# json格式的数据：content-type : application/json,使用json传参
# 具体使用data还是json传参，要看接口是怎么定义的
# httpbin.org 是一个测试网站，不管发送什么类型的数据，
# 这个接口将发送的请求，封装成json格式的饭会
url = "http://www.httpbin.org/post"
cs = {"mobilephone":"admin","pwd":"123456"}
r = requests.post(url,data=cs)
print("data传参===",r.text)
r = requests.post(url,json=cs)
print("json传参===",r.text)

# 租车系统，添加车辆
url = "http://127.0.0.1:8088/carRental/car/addCar.action"
# 接口文档中对接口描述不清晰
# 通过界面操作接口对应功能，抓包（Fiddler、浏览器F12）看
cs = {
    'carnumber':1234599,
    'cartype':2222,
    'color':'ty',
    'carimg':'images/defaultcarimage.jpg',
    'description':'huang',
    'price':200,
    'rentprice':10,
    'deposit':2,
    'isrenting':0
}
# 使用接口添加车辆
head = {
    "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/84.0.4147.89 Safari/537.36",
}

# Fiddler 抓脚本的包，设置代理
proxy = {
    "http": "http://127.0.0.1:8088",# http协议，使用这个代理
    "https": "https://127.0.0.1:8088" # http协议，使用这个代理
}
r = requests.post(url,data=cs,header=head)
print(r.text)