from lib.solutions.CHK import checkout_solution


class TestSum():
    """"""
    def test_sum(self):
        assert checkout_solution.checkout('AAABEE') == 160


TestSum().test_sum()
