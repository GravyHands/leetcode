class Solution(object):
    class PointInfo:
        left = -1
        center = -1

    def uniqueLetterString(self, S):
        def _sum_unique_strings(left, center, right):
            right_buffer = right - center - 1
            left_buffer = center - left - 1
            span = left_buffer + 1 + right_buffer
            wiggle = min(left_buffer, right_buffer) + 1

            edges = (wiggle + 1) * wiggle
            remaining_sizes = span - (wiggle * 2)
            mid_sum = remaining_sizes * wiggle

            total = edges + mid_sum

            print "({}, {}, {}) ===> {}".format(left, center, right, total)
            return total

        def _sum_uniques_optimized(left, center, right):
            L = center - left - 1
            R = right - center - 1
            M = min(L, R)
            return (M + 1) * (L + R + 1 - M)

        MODULO = 10 ** 9 + 7

        total_uniques = 0
        letter_infos = [self.PointInfo() for i in xrange(26)]
        for i, s in enumerate(S):
            pos = ord(s) - ord('A')
            point = letter_infos[pos]
            if point.center < 0:
                point.center = i
            else:
                total_uniques += _sum_uniques_optimized(
                    point.left, point.center, i
                )
                total_uniques %= MODULO
                point.left = point.center
                point.center = i

        for letter in letter_infos:
            if letter.center >= 0:
                total_uniques += _sum_uniques_optimized(
                    letter.left, letter.center, len(S)
                )
                total_uniques %= MODULO

        return total_uniques
