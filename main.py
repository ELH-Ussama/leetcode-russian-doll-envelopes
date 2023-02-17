from typing import List, Dict


class Envelope:
    def __init__(self, identifier: int, width: int, height: int) -> None:
        self.id = identifier
        self.width = width
        self.height = height

    def can_contain(self, other: 'Envelope') -> bool:
        return self.width > other.width and self.height > other.height

    def filter_can_contain(self, others: List['Envelope']) -> List['Envelope']:
        can_contain = []

        for other in others:
            if self.can_contain(other):
                can_contain.append(other)

        return can_contain


class Solution:
    @staticmethod
    def init_envelopes(envelopes: List[List[int]]) -> List[Envelope]:
        all_envelopes: List[Envelope] = []

        for i in range(len(envelopes)):
            envelope = envelopes[i]
            all_envelopes.append(Envelope(i, envelope[0], envelope[1]))

        return all_envelopes

    @staticmethod
    def get_envelope_can_contain_map(all_envelopes: List[Envelope]) -> Dict[int, List[int]]:
        envelope_can_contain_map: Dict[int: List[int]] = {}

        for i in range(len(all_envelopes)):
            envelope = all_envelopes[i]
            can_be_contained = envelope.filter_can_contain(all_envelopes)
            ids = [e.id for e in can_be_contained]
            envelope_can_contain_map[i] = ids

        return envelope_can_contain_map

    @staticmethod
    def find_the_biggest_list(lists: Dict[int, List[int]], search_perimeter: List[int]) -> int:
        index_of_biggest = -1
        len_of_biggest = -1

        for i in search_perimeter:
            len_of_current_list = len(lists[i])
            if len_of_current_list > len_of_biggest:
                len_of_biggest, index_of_biggest = len_of_current_list, i

        return index_of_biggest

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        number_of_envelopes = len(envelopes)

        all_envelopes = self.init_envelopes(envelopes)

        envelope_can_contain_map = self.get_envelope_can_contain_map(all_envelopes)

        count = 0
        next_search_perimeter = list(range(number_of_envelopes))
        while len(next_search_perimeter) > 0:
            next_envelop_id = self.find_the_biggest_list(envelope_can_contain_map, next_search_perimeter)
            next_search_perimeter = envelope_can_contain_map[next_envelop_id]
            count += 1

        return count


if __name__ == '__main__':
    print('Hello')
