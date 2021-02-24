import requests

# 接口路径
url = "http://127.0.0.1:8088/carrental/file/uploadFile.action"
# 本地存在文件
file = "D:\workspace\shili\workspace\python\day01\内存图.png"
with open(file,mode='rb') as f:
    # {'name':file - tuple}
    # {'filename': fileobj,'content_type'}
    cs = {"filename": (file,f,"image/png")}
    r = requests.post(url,files=cs)
    print(r.text)

# 租车系统上传图片
url = "http://127.0.0.1:8088/carRental/file/uploadFile.action"
# 本地存在的文件
file = "d:/机械师.jpg"
# rb二进制只读的方式打开
with open(file,mode='rb') as f:
    # {'name':file - tuple}
    # {'filename': fileobj,'content_type'}
    cs = {"mf": (file,f,"image/png")}
    r = requests.post(url,files=cs)
    uploadPath = r.json()['data']['src']
    print(r.text)

# 添加车，使用刚刚上传的图片
url = "http://127.0.0.1:8088/carRental/car/addCar.action"
cs = {
    'carnumber':"陕A2333",'cartype':"面包车",'color':'七彩黄',
    'carimg':uploadPath,'description':'这车太特么黄了，车门还焊死了',
    'price':20000,'rentprice':1000,'deposit':500,'isrenting':0
}
head = {"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"}
r = requests.post(url,data=cs,headers=head)
print(r.text)
# 添加车，使用刚上传的图片
