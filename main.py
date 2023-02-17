from typing import List, Dict, Tuple
import numpy as np


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

    def can_contain(self, other: 'Envelope') -> bool:
        return self.width > other.width and self.height > other.height

    def depth(self, matrix: np.ndarray) -> int:
        if self.computed_depth:
            return self.computed_depth
        if self.children is None or len(self.children) == 0:
            self.computed_depth = 1
            return self.computed_depth
        children_ids = [child.id for child in self.children]
        root_children = [child for child in self.children if not matrix[children_ids, child.id].any()]
        children_depths = [child.depth(matrix) for child in root_children]
        self.computed_depth = 1 + max(children_depths)
        return self.computed_depth


class Solution:
    envelopes: List[Envelope] = None
    matrix: np.ndarray = None

    def get_envelope_can_contain_map(self) -> Dict[int, List[int]]:
        envelope_can_contain_map: Dict[int: List[int]] = {}

        for i in range(len(self.envelopes)):
            ids = [j for j in range(len(self.envelopes)) if self.matrix[i, j]]
            envelope_can_contain_map[i] = ids

        return envelope_can_contain_map

    def compute_envelopes_tree_dependencies(self):
        envelope_can_contain_map = self.get_envelope_can_contain_map()
        for envelope_id in envelope_can_contain_map:
            can_contain = envelope_can_contain_map[envelope_id]
            can_contain_nodes = [self.envelopes[envelope_id] for envelope_id in can_contain]
            self.envelopes[envelope_id].children = can_contain_nodes

    def init_envelopes(self, envelopes: List[Tuple[int, ...]]) -> None:
        all_envelopes: List[Envelope] = []

        for i in range(len(envelopes)):
            envelope = envelopes[i]
            all_envelopes.append(Envelope(i, envelope[0], envelope[1]))

        self.envelopes = all_envelopes

    def init_matrix(self, envelopes: List[Tuple[int, ...]]):
        n = len(envelopes)
        self.matrix = np.zeros((n, n), dtype=bool)
        for i in range(n):
            wi, hi = envelopes[i]
            for j in range(i+1, n):
                wj, hj = envelopes[j]
                self.matrix[i, j] = wi > wj and hi > hj
                self.matrix[j, i] = wj > wi and hj > hi
        for i in range(n):
            for j in range(n):
                i_parent_of_j = self.matrix[i, j]
                if i_parent_of_j:
                    i_children = self.matrix[i]
                    j_children = self.matrix[j]
                    self.matrix[i] = np.logical_and(i_children, np.logical_not(j_children))

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        unique_envelopes = list(set(tuple(e) for e in envelopes))
        self.init_envelopes(unique_envelopes)
        self.init_matrix(unique_envelopes)
        self.compute_envelopes_tree_dependencies()

        root_envelopes = [j for j in range(len(self.matrix)) if not self.matrix[:, j].any()]

        nodes_depths = [self.envelopes[i].depth(self.matrix) for i in root_envelopes]

        return max(nodes_depths)


if __name__ == '__main__':
    print('Hello')
