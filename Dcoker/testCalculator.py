import pytest
import calculator

class TestCalculator:
    def test_Calculator_Add1(self):
        obj = calculator.Calculator()
        out = obj.functionAdd(10, 20)
        assert out == 30

    def test_Calculator_Add2(self):
        obj = calculator.Calculator()
        out = obj.functionAdd(10, 200)
        assert out == 210

    def test_Calculator_Add3(self):
        obj = calculator.Calculator()
        out = obj.functionAdd(50, 20)
        assert out == 70

    def test_Calculator_Add4(self):
        obj = calculator.Calculator()
        out = obj.functionAdd(0.6, 3.6)
        assert out == 4.2

    def test_Calculator_Sub1(self):
        obj = calculator.Calculator()
        out = obj.functionSub(10, 20)
        assert out == -10

    def test_Calculator_Sub2(self):
        obj = calculator.Calculator()
        out = obj.functionSub(200, 10)
        assert out == 190

    def test_Calculator_Sub3(self):
        obj = calculator.Calculator()
        out = obj.functionSub(50, 20)
        assert out == 30

    def test_Calculator_Sub4(self):
        obj = calculator.Calculator()
        out = obj.functionSub(-0.6, -3.6)
        assert out == 3.0

    def test_Calculator_Mul1(self):
        obj = calculator.Calculator()
        out = obj.functionMul(10, 20)
        assert out == 200

    def test_Calculator_Mul2(self):
        obj = calculator.Calculator()
        out = obj.functionMul(10, 200)
        assert out == 2000

    def test_Calculator_Mul3(self):
        obj = calculator.Calculator()
        out = obj.functionMul(50, 20)
        assert out == 1000

    def test_Calculator_Mul4(self):
        obj = calculator.Calculator()
        out = obj.functionMul(0.6, 3.6)
        assert out == 2.16

    def test_Calculator_Div1(self):
        obj = calculator.Calculator()
        out = obj.functionDiv(10, 20)
        assert out == 0.5

    def test_Calculator_Div2(self):
        obj = calculator.Calculator()
        out = obj.functionDiv(10, 200)
        assert out == 0.05

    def test_Calculator_Div3(self):
        obj = calculator.Calculator()
        out = obj.functionDiv(50, 20)
        assert out == 2.5

    def test_Calculator_Div4(self):
        obj = calculator.Calculator()
        out = obj.functionDiv(0.6, 3.6)
        assert out == 0.16666666666666666