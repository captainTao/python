pytest
----------
https://blog.51cto.com/u_14797793/3289589

# 运行指定类下的指定方法
pytest 文件名::类名::方法名
pytest
pytest -v
pytest --markers 查看标记

安装：
pip install -U pytest

Pytest用例设计原则：
-----------------
测试类以Test开头，并且不能带有init方法
以test 开头的函数
以Test开头的类
所有的包pakege必须要有 init .py文件
断言使用assert



"""
pytest命名规则：
    测试文件必须以：
        test_*.py开头
        *_test.py结尾
    测试类以及方法命名规则：
        Test*类包含所有的test_*的方法（注意不能有__init__方法）
        否则pytest会认为这不是一个测试用例而是一个有特殊功能的类
        或者不在class中的test_*的方法
"""


运行：
pycharm运行：
pytest.main(["test.py"])

命令行运行：
pytest test.py
#运行指定类下的指定方法
pytest 文件名::类名::方法名


1.打印输出 -s


2.@pytest.fixture()
fixture(scope='function', params=None, autouse=False, ids=None, name=None)

# https://blog.csdn.net/IT_LanTian/article/details/122896237
# https://blog.csdn.net/weixin_43863765/article/details/120766206
# https://blog.51cto.com/u_14797793/3289589
# https://blog.csdn.net/IT_LanTian/article/details/122896237

@pytest.fixture()
def login():
    print('登录系统')

# 直接使用函数名做为参数传入
def test_01(login):
    print('测试用例一')



3.@pytest.mark.usefixtures("装饰器名")


4.@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
"""
https://blog.csdn.net/ccgshigao/article/details/113102627
"""


5. with assume
"""
https://blog.csdn.net/ccgshigao/article/details/113102627
pip install pytest-assume
多断言，前断言失败后，还会执行
"""



6.@pytest.mark.happy 自定义标签
https://blog.csdn.net/totorobig/article/details/112798884

运行方法
#语法
pytest -m "自定义标签名"
或：
pytest.main(['-m 自定义标签名'])
#示例：
pytest -m "smoke" testmark.py


7.不能有__init__


8.断言 asset后面加，error msg

9.pytest.ini
[pytest];固定写法

;变量名不能错
markers =
    slow: marks tests as slow (deselect with '-m "not slow"', can use or, not, and)
    smoke: Run the smoke test functions for tasks project
    critical: marks as critical
    get: Run the test functions that test tasks.get()
    happy:
    serial

addopts = -vv -s --strict-markers ;多个参数中间空格
testpaths = ./test_case ;多个目录中间空格
python_files = test*.py ;python文件前缀，可自定义
python_classes = Test* ;指定类名
python_functions = test* ;指定方法名,可自定义

标记注册好后，可以通过pytest --markers来查看



pytest.ini
-------------
[pytest]

minversion = 5.0

markers =
    slow: marks tests as slow (deselect with '-m "not slow"', or, not, and expression supported)
    smoke: Run the smoke test functions for tasks project
    critical: mark cases as critical
    failed: mark cases failed
    success: mark cases success
    serial
    uat: uat cases
    system: system test cases


addopts = -vv --strict-markers -s
testpaths = ./python
python_files = test*.py
python_classes = Test*
python_functions = test*

log_cli = 1
log_cli_level = INFO

filterwarnings =
    ignore::urllib3.exceptions.InsecureRequestWarning
    ignore::DeprecationWarning


10.pytest输出logging

log_cli = 1
log_cli_level = INFO

11. @pytest.mark.run
@pytest.mark.run(order=-2)
def test_three():
    assert True

@pytest.mark.run(order=-1)
def test_four():
    assert True

@pytest.mark.run(order=2)
def test_two():
    assert True

@pytest.mark.run(order=1)


12. pytest用例前和用例后


13.allure关键字:
https://www.cnblogs.com/Zhan-W/p/13141219.html

Allure用例描述
使用方法    参数值 参数说明
@allure.epic()  epic描述  定义项目、当有多个项目是使用。往下是feature
@allure.feature()   模块名称    用例按照模块区分，有多个模块时给每个起名字　　
@allure.story() 用例名称    一个用例的描述
@allure.title(用例的标题)    用例标题    一个用例标题
@allure.testcase()  测试用例的连接地址   自动化用例对应的功能用例存放系统的地址
@allure.issue() 缺陷地址    对应缺陷管理系统里边的缺陷地址
@allure.description()   用例描述    对测试用例的详细描述
@allure.step()  操作步骤    测试用例的操作步骤
@allure.severity()  用例等级    blocker  、critical  、normal  、minor  、trivial
@allure.link()  定义连接    用于定义一个需要在测试报告中展示的连接
@allure.attachment()    附件  添加测试报告附件


@allure.title和@allure.dynamic.title


14.参数化读取yaml



15.生成allure报告：

安装模块:pip install allure-pytest
#第一步:生成xml数据
pytest--alluredir=./report/xml testcase.py
#第二步:生成html文件
allure generate--clean ./report/xml -o ./result/html
