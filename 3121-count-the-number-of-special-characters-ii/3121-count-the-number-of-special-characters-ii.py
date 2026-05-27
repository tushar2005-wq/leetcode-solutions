class Solution(object):
    def numberOfSpecialChars(self, word):
        first_upper = {}
        last_lower = {}

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                if ch not in first_upper:
                    first_upper[ch] = i

        ans = 0

        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)

            if lower in last_lower and upper in first_upper:
                if last_lower[lower] < first_upper[upper]:
                    ans += 1

        return ans
        """
        :type word: str
        :rtype: int
        """
        