from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        def _get_initial_dict(nums):
            num_count = defaultdict(lambda: 0)
            for num in nums:
                num_count[num] += 1
            return num_count

        def _calc_sum_dict(left, right):
            sum_dict = defaultdict(lambda: 0)
            for l_num, l_count in left.items():
                for r_num, r_count in right.items():
                    summed = l_num + r_num
                    sum_dict[summed] += l_count * r_count
            return sum_dict
        # dictionaries are internally hashmaps, so constant time access
        # O(4n)
        a = _get_initial_dict(A)
        b = _get_initial_dict(B)
        c = _get_initial_dict(C)
        d = _get_initial_dict(D)

        # O(2n^2)
        ab = _calc_sum_dict(a, b)
        cd = _calc_sum_dict(c, d)

        # O(n^2)
        total = 0
        for num, count in ab.items():
            match = -num
            total += count * cd.get(match, 0)
        return total
