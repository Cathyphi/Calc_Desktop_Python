import unittest
from presenter import *

class TestSmartCalc(unittest.TestCase):
    def test1(self):
        f = Model()
        s = "-33+(-4+8)*2"
        x = f.Parsing(s)
        res = -25.0
        self.assertEqual(res, x)

    def test2(self):
        f = Model()
        s = "98/89-8"
        x = f.Parsing(s)
        res = -6.898876404494382
        self.assertEqual(res, x)

    def test3(self):
        f = Model()
        s = "33-(4+8)*2-876.567+(987-473)/9"
        x = f.Parsing(s)
        res = -810.4558888888889
        self.assertEqual(res, x)

    def test4(self):
        f = Model()
        s = "(58-9)+(32*(4-7)+(74*(3/9)))"
        x = f.Parsing(s)
        res = -22.333333333333343
        self.assertEqual(res, x)

    def test5(self):
        f = Model()
        s = "78^5+13%7"
        x = f.Parsing(s)
        res = 2887174374.0
        self.assertEqual(res, x)

    def test6(self):
        f = Model()
        s = "834958.2645%1425.235%685.3"
        x = f.Parsing(s)
        res = 510.489500000107
        self.assertEqual(res, x)

    def test7(self):
        f = Model()
        s = "sin(1+0.678)"
        x = f.Parsing(s)
        res = 0.9942591874714983
        self.assertEqual(res, x)

    def test8(self):
        f = Model()
        s = "cos(1+cos(cos(3+4*5)+10)/2)"
        x = f.Parsing(s)
        res = 0.8773671442085055
        self.assertEqual(res, x)

    def test9(self):
        f = Model()
        s = "acos(0.369852)"
        x = f.Parsing(s)
        res = 1.191946606688294
        self.assertEqual(res, x)

    def test10(self):
        f = Model()
        s = "asin(0.2)"
        x = f.Parsing(s)
        res = 0.2013579207903308
        self.assertEqual(res, x)

    def test11(self):
        f = Model()
        s = "tan(2023.2023)"
        x = f.Parsing(s)
        res = 0.01663262169078549
        self.assertEqual(res, x)

    def test12(self):
        f = Model()
        s = "atan(0.2023)"
        x = f.Parsing(s)
        res = 0.19960611696272892
        self.assertEqual(res, x)

    def test13(self):
        f = Model()
        s = "log(2023.2023)"
        x = f.Parsing(s)
        res = 3.3060393100476673
        self.assertEqual(res, x)

    def test14(self):
        f = Model()
        s = "ln(2023.2023)"
        x = f.Parsing(s)
        res = 7.612436832168079
        self.assertEqual(res, x)

    def test15(self):
        f = Model()
        s = "sqrt(2023)"
        x = f.Parsing(s)
        res = 44.97777228809804
        self.assertEqual(res, x)

    def test16(self):
        f = Model()
        s = "-3/9.33+(-3-3.123456+3)"
        x = f.Parsing(s)
        res = -3.4449994083601285
        self.assertEqual(res, x)

    def test17(self):
        f = Model()
        s = "5+(-5)*(-1+6)"
        x = f.Parsing(s)
        res = -20
        self.assertEqual(res, x)

    def test18(self):
        f = Model()
        s = "4E4"
        x = f.Parsing(s)
        res = 40000
        self.assertEqual(res, x)


if __name__ == "__main__":
    unittest.main()
