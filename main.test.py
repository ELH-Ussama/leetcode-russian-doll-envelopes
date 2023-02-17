import unittest
import timeout_decorator

from main import Solution
from test_cases.test_case_70_big_input import big_list_of_envelopes


class TestSolution(unittest.TestCase):
    def test_should_not_russian_doll_envelopes_with_the_same_size(self):
        # GIVEN
        envelopes = [[1, 1], [1, 1], [1, 1]]

        # WHEN
        max_envelopes = Solution().maxEnvelopes(envelopes)

        # THEN
        self.assertEqual(max_envelopes, 1)

    def test_should_russian_doll_all_ordered_envelops(self):
        # GIVEN
        envelopes = [[1, 1], [2, 2], [3, 3]]

        # WHEN
        max_envelopes = Solution().maxEnvelopes(envelopes)

        # THEN
        self.assertEqual(max_envelopes, 3)

    def test_should_not_russian_doll_two_envelopes_with_the_same_height(self):
        # GIVEN
        envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]

        # WHEN
        max_envelopes = Solution().maxEnvelopes(envelopes)

        # THEN
        self.assertEqual(max_envelopes, 3)

    def test_should_not_russian_doll_two_envelopes_with_the_same_width(self):
        # GIVEN
        envelopes = [[5, 4], [6, 7], [8, 7], [2, 3]]

        # WHEN
        max_envelopes = Solution().maxEnvelopes(envelopes)

        # THEN
        self.assertEqual(max_envelopes, 3)

    def test_should_russian_doll_the_deepest_tree(self):
        # GIVEN
        envelopes = [[8, 3], [3, 20], [15, 5], [11, 2], [19, 6], [9, 18], [1, 19], [13, 3], [14, 20], [6, 7]]

        # WHEN
        max_envelopes = Solution().maxEnvelopes(envelopes)

        # THEN
        self.assertEqual(max_envelopes, 4)

    @timeout_decorator.timeout(1)
    def test_Solution_maxEnvelopes_should_not_exceed_1s_time_limit_for_input_of_size_404(self):
        # GIVEN
        envelopes = big_list_of_envelopes

        # WHEN
        max_envelopes = Solution().maxEnvelopes(envelopes)

        # THEN
        self.assertEqual(max_envelopes, 35)


if __name__ == '__main__':
    unittest.main()
