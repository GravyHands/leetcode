class Solution(object):
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    INT_OVERFLOW_LENGTH = len(str(INT_MAX)) + 1

    # retaining this awful argument name in case it is passed by keyword
    def myAtoi(self, str):
        return self._cast(str)

    def _cast(self, a_in):
        def answer(sign, digits):
            num = int("%s%s" % (sign, digits))
            return min(max(self.INT_MIN, num), self.INT_MAX)

        sign = ''

        index = end = 0
        for a in a_in:
            if a in (' ', '-', '+'):
                index += 1
                if a != ' ':
                    sign = a
                    break
                continue
            break

        try:
            while a_in[index] == '0':
                index += 1
        except:
            return 0

        end = index
        try:
            while (end - index) < (self.INT_OVERFLOW_LENGTH) and a_in[end].isdigit():
                end += 1
        except:
            pass
        return answer(sign, a_in[index:end] or '0')

# The import is down here so it is easier to
# quickly copy the whole implementation (Shift+Cmd+UpArrow)
# to paste on the site
import sys

print Solution().myAtoi(sys.argv[1])
