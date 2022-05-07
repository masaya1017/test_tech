import unittest


class Person:
    # 税率
    tax_rate = 0.7

    # コンストラクタ
    # gross_income⇒税引き前の所得
    def __init__(self, first_name, last_name, gross_income):
        self.first_name = first_name
        self.last_name = last_name
        self.gross_income = gross_income
    # property(データを保持したり、返すことが可能)

    @property
    def email(self):
        return f'{self.first_name}_{self.last_name}@gmail.com'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def net_income(self):
        return int(self.gross_income*self.tax_rate)


class TestPerson(unittest.TestCase):
    # 毎回呼ばれる関数(テストごとに初期化されて実行)
    def setUp(self):
        self.person = Person('Taro', 'Yamada', 1000)

    # テストごとに呼び出される(今回は三回分)
    def tearDown(self):
        print('tearDown called \n')
    # テスト前に呼び出される。（一回のみ)

    @classmethod
    def setUpClass(cls):
        print('start \n')
        cls.answer_email = ['Taro_Yamada@gmail.com', 'Taro_Tanaka@gmail.com']
    # テスト後に呼び出される（一回のみ)

    @classmethod
    def tearDownClass(cls):
        print('end \n')

    def test_email(self):
        # personクラスのオブジェクト化
        # オブジェクト化時に、引数に渡されたデータはinitによって保持される。
        #person = Person('Taro', 'Yamada', 1000)
        # getプロパティの実行とテスト
        self.assertEqual(self.person.email, self.answer_email[0])
        # setプロパティの実行
        self.person.last_name = 'Tanaka'
        # getプロパティの実行とテスト
        self.assertEqual(self.person.email, self.answer_email[1])

    def test_full_name(self):
        # personクラスのオブジェクト化
        # オブジェクト化時に、引数に渡されたデータはinitによって保持される。
        #person = Person('Taro', 'Yamada', 1000)
        # getプロパティの実行とテスト
        self.assertEqual(self.person.full_name, 'Taro Yamada')
        # setプロパティの実行
        self.person.last_name = 'Tanaka'
        # getプロパティの実行とテスト
        self.assertEqual(self.person.full_name, 'Taro Tanaka')

    def test_net_income(self):
        # personクラスのオブジェクト化
        # オブジェクト化時に、引数に渡されたデータはinitによって保持される。
        #person = Person('Taro', 'Yamada', 1000)
        # getプロパティの実行とテストの実行
        self.assertEqual(self.person.net_income, 700)


if __name__ == '__main__':
    # ユニットテスト（単体テスト）の実行
    unittest.main()
