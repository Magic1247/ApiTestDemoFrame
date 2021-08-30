import allure
import pytest
import requests

from utils.commonlib import get_test_data
from utils.readConfig import env

cases, parameters = get_test_data("F:\\PycahrmProject\\api_pytest\\data\\test_in_books.yml")
list_params = list(parameters)

@allure.feature('查询书本功能')
class TestInBooks(object):
    @pytest.mark.parametrize("case,http,expected", list(list_params), ids=cases)
    @allure.story('查询')
    @allure.step('请求测试接口')
    def test_in_books(self, env, case, http, expected):
        # print(case)
        # print(expected)
        r = requests.request(http["method"],
                             url=env["host"]["localhost"] + http["path"],
                             headers=http["headers"],
                             params=http["params"])
        response = r.json()
        print(r.json())
        assert response[0]["bookName"] == expected['response']["bookName"]
        assert response[0]["detail"] == expected['response']["detail"]
        assert response[0]["bookID"] == expected['response']["bookID"]
