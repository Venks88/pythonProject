import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def outer(order, innerClass):
    order.append("Outer")

class TestInner:
    @pytest.fixture
    def innerClass(self, order):
        order.append("Inner");

    def test_innerClass(self, order, outer):
        assert order == ["Inner", "Outer"]

class TestInnerClass2:
    @pytest.fixture
    def innerClass(self, order):
        order.append("Inner2")

    def test_innerclass(self, order, outer):
        assert order == ["Inner2", "Outer"]