import unittest
# calc.pyを参照して、各関数を呼び出している。
from calc import add, divide, substract, multiply
# ユニットテストのモジュールを継承させる。


class TestCalc(unittest.TestCase):
    # 必ずメソッドには[test]を付けること
    def test_add(self):
        # addメソッドを呼び出して、計算結果が妥当かを確認。
        self.assertEqual(add(10, 5), 15)

    def test_substract(self):
        self.assertEqual(substract(10, 5), 5)

    def test_multiply(self):
        # あえて間違った計算を行っている
        self.assertEqual(multiply(10, 5), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        # エラーが出現しているかも確認できる。
        with self.assertRaises(ZeroDivisionError):
            divide(10, 2)


if __name__ == '__main__':
    # ユニットテスト（単体テスト）の実行
    unittest.main()
