class Solution(object):
    def isValid(self, s):
        stack=[]
        matching={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in matching.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if top!=matching[ch]:
                    return False
        return len(stack)==0
        """
        :type s: str
        :rtype: bool
        """
        