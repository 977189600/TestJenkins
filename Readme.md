接口功能自动化测试程序（Python版） 运行环境：

##### python3
##### pytest
##### allure report
##### git

依赖准备： pip install allure-pytest

运行命令： pytest -sv test/weather_test.py --alluredir ./allure-results  PythonApi

接口功能自动化测试项目介绍：

1、接口功能测试地址：http://www.weather.com.cn/data/cityinfo/

2、接口功能：获取对应城市的天气预报

3、功能包：HttpClient

4、请求方法：Get
