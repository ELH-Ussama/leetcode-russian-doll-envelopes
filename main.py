from typing import List


class Solution:
    @staticmethod
    def envelope_size(envelope: List[int]) -> int:
        return envelope[0] + envelope[1]

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sizes = []

        for envelope in envelopes:
            sizes.append(self.envelope_size(envelope))

        return len(set(sizes))


if __name__ == '__main__':
    print('Hello')
