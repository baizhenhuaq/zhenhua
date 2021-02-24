import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param

def test_login(baserequest,url,login_data,db_info):
    # 初始化环境
    MySqlOp.delete_user(db_info,login_data['regdata']['mobilephone'])
    # 注册用户
    r = Member.register(baserequest,url,login_data['regdata'])
    # 登录
    r = Member.login(baserequest,url,login_data['logindata'])
    # 检查结果
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['msg'] == login_data['expect']['msg']
    # 删除注册用户
    MySqlOp.delete_user(db_info,login_data['regdata']['mobilephone'])
