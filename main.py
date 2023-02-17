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


class Node:
    children: List['Node'] or None

    def __init__(self, children=None) -> None:
        if children is None:
            children = []
        self.children = children

    def depth(self) -> int:
        if self.children is None or len(self.children) == 0:
            return 1
        children_depths = [child.depth() for child in self.children]
        return 1 + max(children_depths)


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

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        number_of_envelopes = len(envelopes)

        all_envelopes = self.init_envelopes(envelopes)

        envelope_can_contain_map = self.get_envelope_can_contain_map(all_envelopes)

        nodes = [Node() for _ in range(number_of_envelopes)]

        for envelope_id in envelope_can_contain_map:
            can_contain = envelope_can_contain_map[envelope_id]
            can_contain_nodes = [nodes[envelope_id] for envelope_id in can_contain]
            nodes[envelope_id].children = can_contain_nodes

        nodes_depths = [node.depth() for node in nodes]

        return max(nodes_depths)


if __name__ == '__main__':
    print('Hello')
