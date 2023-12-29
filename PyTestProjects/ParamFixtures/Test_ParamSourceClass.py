from ParamSourceClass import ParamSourceClass
import pytest
from unittest.mock import Mock, patch

@pytest.fixture()
def classObj():
    print("Setting up resources ...")
    yield ParamSourceClass()
    print("Tearing down resources ...")

@pytest.fixture()
def mockClassObj():
    yield 77

class Test_ParamSourceClass:

    @pytest.mark.parametrize("a,b", [(1, 2), (3, 4), (5, 6)])
    def test_addition(self, classObj, a, b):
        result = classObj.sum(a,b)
        assert result > 1

    def test_subtraction(self, classObj):
        result = classObj.diff(5, 3)
        assert result == 2

    def test_multiplication(self, classObj):
        result = classObj.mul(5, 3)
        assert result == 15

    def test_division(self, classObj):
        result = classObj.div(10, 2)
        assert result == 5

    @patch('ParamSourceClass.ParamSourceClass')
    def test_mockSum(self, mockClassObj):
        result = classObj
        assert result == 77