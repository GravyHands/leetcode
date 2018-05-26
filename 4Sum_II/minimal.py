from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        ab = defaultdict(0)
        for a in A:
            for b in B:
                ab[a+b] += 1

        total = 0
        for c in C:
            for d in D:
                total += ab.get(-(c+d), 0)

        return total
