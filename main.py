from typing import List


class Envelope:
    children: List['Envelope'] or None
    computed_depth: int or None

    def __init__(self, children: List['Envelope'] = None) -> None:
        self.computed_depth = None
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
    n: int

    def compute_envelopes_tree_dependencies(self):
        for envelope_id in range(self.n):
            can_contain = self.envelopes_children[envelope_id]
            can_contain_nodes = [self.envelopes[envelope_id] for envelope_id in can_contain]
            self.envelopes[envelope_id].children = can_contain_nodes

    def init_envelopes(self) -> None:
        self.envelopes = []

        for i in range(self.n):
            self.envelopes.append(Envelope())

    def init_parent_children_map(self, envelopes: List[List[int]]) -> None:
        self.envelopes_children = [[] for _ in range(self.n)]
        for i in range(self.n):
            wi, hi = envelopes[i]
            for j in range(i + 1, self.n):
                wj, hj = envelopes[j]
                i_parent_of_j = wi > wj and hi > hj
                if i_parent_of_j:
                    self.envelopes_children[i].append(j)
                    continue
                j_parent_of_i = wj > wi and hj > hi
                if j_parent_of_i:
                    self.envelopes_children[j].append(i)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        self.n = len(envelopes)
        self.init_envelopes()
        self.init_parent_children_map(envelopes)
        self.compute_envelopes_tree_dependencies()

        nodes_depths = [self.envelopes[i].depth() for i in range(self.n)]

        return max(nodes_depths)


if __name__ == '__main__':
    print('Hello')
