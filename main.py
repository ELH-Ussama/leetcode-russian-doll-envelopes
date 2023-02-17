from typing import List


class Node:
    children: List['Node'] = []
    computed_depth: int or None

    def __init__(self) -> None:
        self.computed_depth = None

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
    graph: List[Node] = None
    envelopes_children: List[List[int]]
    n: int

    def compute_envelopes_graph_dependencies(self):
        for envelope_id in range(self.n):
            can_contain = self.envelopes_children[envelope_id]
            can_contain_nodes = [self.graph[envelope_id] for envelope_id in can_contain]
            self.graph[envelope_id].children = can_contain_nodes

    def init_graph(self) -> None:
        self.graph = []

        for i in range(self.n):
            self.graph.append(Node())

    def compute_envelopes_children(self, envelopes: List[List[int]]) -> None:
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
        self.init_graph()
        self.compute_envelopes_children(envelopes)
        self.compute_envelopes_graph_dependencies()

        nodes_depths = [self.graph[i].depth() for i in range(self.n)]

        return max(nodes_depths)


if __name__ == '__main__':
    print('Hello')
