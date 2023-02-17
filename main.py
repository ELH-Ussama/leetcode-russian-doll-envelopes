from typing import List, Tuple


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

    def depth(self) -> int:
        if self.computed_depth:
            return self.computed_depth
        if self.children is None or len(self.children) == 0:
            self.computed_depth = 1
            return self.computed_depth
        children_depths = [child.depth() for child in self.children]
        self.computed_depth = 1 + max(children_depths)
        return self.computed_depth


class Solution:
    envelopes: List[Envelope] = None
    envelopes_children: List[List[int]]

    def compute_envelopes_tree_dependencies(self):
        for envelope_id in range(len(self.envelopes)):
            can_contain = self.envelopes_children[envelope_id]
            can_contain_nodes = [self.envelopes[envelope_id] for envelope_id in can_contain]
            self.envelopes[envelope_id].children = can_contain_nodes

    def init_envelopes(self, envelopes: List[Tuple[int, ...]]) -> None:
        all_envelopes: List[Envelope] = []

        for i in range(len(envelopes)):
            envelope = envelopes[i]
            all_envelopes.append(Envelope(i, envelope[0], envelope[1]))

        self.envelopes = all_envelopes

    def init_parent_children_map(self, envelopes: List[Tuple[int, ...]]) -> None:
        n = len(envelopes)
        self.envelopes_children = [[] for _ in range(n)]
        for i in range(n):
            wi, hi = envelopes[i]
            for j in range(i + 1, n):
                wj, hj = envelopes[j]
                i_parent_of_j = wi > wj and hi > hj
                if i_parent_of_j:
                    self.envelopes_children[i].append(j)
                    continue
                j_parent_of_i = wj > wi and hj > hi
                if j_parent_of_i:
                    self.envelopes_children[j].append(i)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        unique_envelopes = list(set(tuple(e) for e in envelopes))
        self.init_envelopes(unique_envelopes)
        self.init_parent_children_map(unique_envelopes)
        self.compute_envelopes_tree_dependencies()

        nodes_depths = [self.envelopes[i].depth() for i in range(len(unique_envelopes))]

        return max(nodes_depths)


if __name__ == '__main__':
    print('Hello')
