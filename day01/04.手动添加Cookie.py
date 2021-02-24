'''
Cookie 用来识别客户
'''

import requests

# 没有登录时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上Cookie信息
head = {
"Cookie": '_ga=GA1.2.1569596273.1611729534; __auc=70b0f6521774291012a9547f9f5; MEIQIA_TRACK_ID=1ndpfzVWNAKqDDGaU64ZZUp9PuB; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611730281,1611730449,1611730524,1611818530; __asc=be7df3b617747def40f492ed43e; MEIQIA_VISIT_ID=1ngjGPVlhN14ycB7Uc1xeZ7QREV; BAGSESSIONID=fcf6c311-55f5-4612-b6df-a421731519f0; JSESSIONID=E71C7B1DD29BE160BF5FF64D7FF7616B; _gid=GA1.2.1726590345.1611818539; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611819265'
}
r = requests.get(url,headers= head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

'''
缺点：

'''