class Solution(object):
    def processStr(self, s, k):
        lengths = [0] * (len(s) + 1)

        curr = 0
        for i, ch in enumerate(s):
            if ch.islower():
                curr += 1
            elif ch == "*":
                curr = max(0, curr - 1)
            elif ch == "#":
                curr *= 2

            lengths[i + 1] = curr

        if k >= curr:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev = lengths[i]

            if ch.islower():
                if k == prev:
                    return ch

            elif ch == "*":
                pass

            elif ch == "#":
                if k >= prev:
                    k -= prev

            elif ch == "%":
                k = prev - 1 - k

        return '.'

        """
        :type s: str
        :type k: int
        :rtype: str
        """
        