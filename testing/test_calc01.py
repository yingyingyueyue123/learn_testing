import os

import pytest
import yaml

from pythoncode.calculator import Calculator

import pytest_ordering


# 读取测试数据
def get_datas():
    # 获取测试数据的绝对路径
    mydatapath = os.path.dirname(__file__) + "/datas/calc.yml"
    with open(mydatapath, encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        addmyids = mydatas['add']['myids']
        subdatas = mydatas['sub']['datas']
        submyids = mydatas['sub']['myids']
        muldatas = mydatas['mul']['datas']
        mulmyids = mydatas['mul']['myids']
        divdatas = mydatas['div']['datas']
        divmyids = mydatas['div']['myids']
    return [adddatas, addmyids, subdatas, submyids, muldatas, mulmyids, divdatas, divmyids]


"""
# 使用数据
@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_datas(request):
    return request.param



@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")
"""


class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,except_result', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, except_result):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert except_result == result

    @pytest.mark.sub
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,except_result', get_datas()[2], ids=get_datas()[3])
    def test_sub(self, a, b, except_result):
        # calc = Calculator()
        result = self.calc.sub(a, b)
        assert except_result == result

    @pytest.mark.mul
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,except_result', get_datas()[4], ids=get_datas()[5])
    def test_mul(self, a, b, except_result):
        # calc = Calculator()
        result = self.calc.mul(a, b)
        assert except_result == result

    @pytest.mark.div
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,except_result', get_datas()[6], ids=get_datas()[7])
    def test_div(self, a, b, except_result):
        # calc = Calculator()
        result = self.calc.div(a, b)
        assert except_result == result
