from typing import List


class Envelope:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def cascade_envelope(self, other: 'Envelope') -> List['Envelope']:
        if other.width > self.width and other.height > self.height:
            new_parent = True
            # new_parent logic
            return True

        if self.width > other.width and self.height > other.height:
            can_go_lower = True
            # can go lower logic
            return True

        return False

    def depth(self) -> int:
        pass


class Solution:
    def maxEnvelopes(self, envelopes_sizes: List[List[int]]) -> int:
        trees: List[Envelope] = []
        for envelope_size in envelopes_sizes:
            envelope = Envelope(envelope_size[0], envelope_size[1])
            is_root = True
            for i in range(len(trees)):
                other = trees[i]
                added = other.cascade_envelope(envelope)
                if len(added) > 2:
                    is_root = False

            if is_root:
                trees.append(envelope)

        return max([e.depth() for e in trees])
