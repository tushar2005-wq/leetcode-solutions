class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            while len(stack)>0 and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if not stack:
                ans[i]=0
            else:
                ans[i]=stack[-1]-i
            stack.append(i)
        return ans

        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        