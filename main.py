from typing import List, Dict


class Envelope:
    children: List['Envelope'] or None
    computed_depth: int or None

    def __init__(self, identifier: int, width: int, height: int, children: List['Envelope'] = None) -> None:
        self.computed_depth = None
        self.id = identifier
        self.width = width
        self.height = height
        if children is None:
            children = []
        self.children = children

    def can_fit_in(self, other: 'Envelope') -> bool:
        return self.width < other.width and self.height < other.height

    def can_fit_in_at_least_one(self, others: List['Envelope']) -> bool:
        for other in others:
            if self.can_fit_in(other):
                return True
        return False

    def can_contain(self, other: 'Envelope') -> bool:
        return self.width > other.width and self.height > other.height

    def filter_can_contain(self, others: List['Envelope']) -> List['Envelope']:
        can_contain = []

        for other in others:
            if self.can_contain(other):
                can_contain.append(other)

        return can_contain

    def depth(self) -> int:
        if self.computed_depth:
            return self.computed_depth
        if self.children is None or len(self.children) == 0:
            self.computed_depth = 1
            return self.computed_depth
        root_children = [child for child in self.children if not child.can_fit_in_at_least_one(self.children)]
        children_depths = [child.depth() for child in root_children]
        self.computed_depth = 1 + max(children_depths)
        return self.computed_depth


class Solution:
    envelopes: List[Envelope] = None

    def get_envelope_can_contain_map(self) -> Dict[int, List[int]]:
        envelope_can_contain_map: Dict[int: List[int]] = {}

        for i in range(len(self.envelopes)):
            envelope = self.envelopes[i]
            can_be_contained = envelope.filter_can_contain(self.envelopes)
            ids = [e.id for e in can_be_contained]
            envelope_can_contain_map[i] = ids

        return envelope_can_contain_map

    def compute_envelopes_tree_dependencies(self):
        envelope_can_contain_map = self.get_envelope_can_contain_map()
        for envelope_id in envelope_can_contain_map:
            can_contain = envelope_can_contain_map[envelope_id]
            can_contain_nodes = [self.envelopes[envelope_id] for envelope_id in can_contain]
            self.envelopes[envelope_id].children = can_contain_nodes

    def init_envelopes(self, envelopes: List[List[int]]) -> None:
        all_envelopes: List[Envelope] = []

        for i in range(len(envelopes)):
            envelope = envelopes[i]
            all_envelopes.append(Envelope(i, envelope[0], envelope[1]))

        self.envelopes = all_envelopes
        self.compute_envelopes_tree_dependencies()

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        self.init_envelopes(envelopes)

        root_envelopes = [e.id for e in self.envelopes if not e.can_fit_in_at_least_one(self.envelopes)]

        nodes_depths = [self.envelopes[i].depth() for i in root_envelopes]

        return max(nodes_depths)


if __name__ == '__main__':
    print('Hello')
