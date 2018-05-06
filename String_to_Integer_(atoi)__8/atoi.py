class Solution(object):
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    MAX_INT_LENGTH = len(str(INT_MAX))

    # retaining this awful argument name in case it is passed by keyword
    def myAtoi(self, str):
        return self._better_naming(str)

    def _better_naming(self, a_in):
        a_in = a_in.lstrip(' ')
        if not a_in:
            return 0

        sign = ''
        if a_in[0] in ('-', '+'):
            sign = a_in[0]
            a_in = a_in[1:]
        a_in = a_in.lstrip('0')
        if not a_in or not a_in[0].isdigit():
            return 0

        a_in = a_in[:self.MAX_INT_LENGTH + 1]
        digits = ''
        for num in a_in:
            if not num.isdigit():
                break
            digits += num

        i_out = int("%s%s" % (sign, digits))
        return max(min(self.INT_MAX, i_out), self.INT_MIN)


import sys

print Solution().myAtoi(sys.argv[1])
