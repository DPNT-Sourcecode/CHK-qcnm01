import sys
# sys.path.append("/Users/arthur/Documents/coding_test/accelerate_runner/")
from lib.solutions.SUM import sum_solution


class TestSum:
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        assert sum_solution.compute(2, 5) == 7


TestSum().test_sum()


