'''
pytest命名约束：
1、文件用test_开头
2.类用Test开头
3、函数或方法用test_开头
'''
url_reg = "http://jy001:8081/futureloan/mvc/api/member/register"
url_log = "http://jy001:8081/futureloan/mvc/api/member/login"

def test_register_001():
    cs = {
        "regname": "requests_test"
    }
    assert "code" == "20103"
    print("都不填的脚本")

def test_register_002():
    cs = {

        "pwd": "12345",
        "regname": "requests_test"
    }
    assert "code" == "20108"
    print("不填手机号，密码位不足6位的脚本")
def test_register_003():
    cs = {

        "pwd": "123456",
        "regname": "requests_test"
    }
    assert "code" == "20103"
    print("不填手机号，密码位数6位的脚本")
def test_register_004():
    cs = {

        "pwd": "1234567890abcdef12",
        "regname": "requests_test"
    }
    assert "code" == "20103"
    print("不填手机号，密码位数为18的脚本")
def test_register_005():
    cs = {

        "pwd": "1234567890abcdef123",
        "regname": "requests_test"
    }
    assert "code" == "20108"
    print("不填手机号，密码位数为19的脚本")

def test_register_006():
    cs = {
        "mobilephone": "18012345678",
        "regname": "requests_test"
    }
    assert "code" == "20103"
    print("填写已注册的手机号，不填密码的脚本")

def test_register_007():
    cs = {
        "mobilephone": "18012345678",
        "pwd": "12345",
        "regname": "requests_test"
    }
    assert "code" == "20108"
    print("填写已注册手机号，密码位数为5的脚本")

def test_register_008():
    cs = {
        "mobilephone": "18012345678",
        "pwd": "123456",
        "regname": "requests_test"
    }
    assert "code" == "20110"
    print("填写已注册手机号，密码位数为6的脚本")

def test_register_009():
    cs = {
        "mobilephone": "18012345678",
        "pwd": "1234567890abcdef12",
        "regname": "requests_test"
    }
    assert "code" == "20110"
    print("填写已注册手机号，密码位数为18的脚本")

def test_register_010():
    cs = {
        "mobilephone": "18012345678",
        "pwd": "1234567890abcdef123",
        "regname": "requests_test"
    }
    assert "code" == "20108"
    print("填写已注册手机号，密码位数为19的脚本")

def test_register_011():
    cs = {
        "mobilephone": "18012345679",
        "regname": "requests_test"
    }
    assert "code" == "20103"
    print("填写新手机号，不填密码的脚本")
def test_register_012():
    cs = {
        "mobilephone": "18012345679",
        "pwd": "12345",
        "regname": "requests_test"
    }
    assert "code" == "20108"
    print("填写新手机号，密码位数为5的脚本")
def test_register_013():
    cs = {
        "mobilephone": "18012345679",
        "pwd": "1234567890abcdef123",
        "regname": "requests_test"
    }
    assert "code" == "20108"
    print("填写新手机号，密码位数为18的脚本")
def test_register_014():
    cs = {
        "mobilephone": "18012345679",
        "pwd": "123456",
        "regname": "requests_test"
    }
    assert "code" == "10001"
    print("注册成功的脚本")
def test_register_015():
    cs = {
        "mobilephone": "18012345672",
        "pwd": "1234567890abcdef12",
        "regname": "requests_test"
    }
    assert "code" == "10001"
    print("注册成功的脚本")

def test_register_00():
    print("手机hao号码格式不正确")

def test_register_00():
    assert "" in ""
    assert "" == ""
    print("密码不足5位")

def test_login_001():
    print("登录成功")