class Solution(object):
    def detectCapitalUse(self, word):
        def allcapital(shabd):
            for i in shabd:
                if i.islower():
                    return False
            return True
        def allsmall(shabd):
            for i in shabd:
                if i.isupper():
                    return False
            return True
        def firstcapital(shabd):
            if shabd[0].isupper() and allsmall(shabd[1:]):
                return True
            return False
        return allcapital(word) or allsmall(word) or firstcapital(word)
        """
        :type word: str
        :rtype: bool
        """
        