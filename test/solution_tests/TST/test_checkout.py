from lib.solutions.CHK import checkout_solution


class TestCheckout:
    """"""
    def test_chk1(self):
        assert checkout_solution.checkout('AAAB') == 160

    def test_chk2(self):
        """
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        +------+-------+------------------------+
        """
        assert checkout_solution.checkout('AAABEE') == 210
        assert checkout_solution.checkout('AAAAA') == 200

    def test_chk3(self):
        """
        +------+-------+------------------------+
        | Item | Price | Special offers         |
        +------+-------+------------------------+
        | A    | 50    | 3A for 130, 5A for 200 |
        | B    | 30    | 2B for 45              |
        | C    | 20    |                        |
        | D    | 15    |                        |
        | E    | 40    | 2E get one B free      |
        | F    | 10    | 2F get one F free      |
        +------+-------+------------------------+
        """
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('AAAAA') == 200

    def test_chk4(self):
        checkout_solution.checkout('UUUUU')


TestCheckout().test_chk4()


