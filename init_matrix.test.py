import unittest

from main import Solution


class InitMatrix(unittest.TestCase):
    def test_case_1(self):
        # GIVEN
        envelopes = [[1, 1], [2, 2], [3, 3]]

        # WHEN
        init_matrix = Solution.get_init_matrix(envelopes)

        # THEN
        expected = [[False, False, False],
                    [True, False, False],
                    [False, True, False]]
        self.assertListEqual(init_matrix.tolist(), expected)

    def test_case_2(self):
        # GIVEN
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]

        # WHEN
        init_matrix = Solution.get_init_matrix(envelopes)

        # THEN
        expected = [[False, False, False, True],
                    [False, False, False, True],
                    [True, False, False, False],
                    [False, False, False, False]]
        self.assertListEqual(init_matrix.tolist(), expected)


if __name__ == '__main__':
    unittest.main()
