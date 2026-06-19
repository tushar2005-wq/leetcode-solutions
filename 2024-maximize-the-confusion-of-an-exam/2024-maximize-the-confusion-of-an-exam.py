class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        def longest(ch):
            l=0
            ans=0
            changes=0
            for r in range(len(answerKey)):
                if answerKey[r]!=ch:
                    changes+=1
                while changes>k:
                    if answerKey[l]!=ch:
                        changes-=1
                    l+=1
                ans=max(ans,r-l+1)
            return ans
        return max(longest('T'),longest('F'))
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        