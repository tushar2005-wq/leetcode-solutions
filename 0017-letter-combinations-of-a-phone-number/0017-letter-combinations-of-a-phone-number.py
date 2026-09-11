class Solution(object):
    def letterCombinations(self, digits):
        ans=[]
        freq={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits)==1:
            return freq[digits]
        if len(digits)==2:
            first=freq[digits[0]]
            second=freq[digits[1]]
            for i in range(len(first)):
                for j in range(len(second)):
                    ans.append(first[i]+second[j])
            return ans
        if len(digits)==3:
            first=freq[digits[0]]
            second=freq[digits[1]]
            third=freq[digits[2]]
            for i in range(len(first)):
                for j in range(len(second)):
                    for k in range(len(third)):
                        ans.append(first[i]+second[j]+third[k])
            return ans
        if len(digits)==4:
            first=freq[digits[0]]
            second=freq[digits[1]]
            third=freq[digits[2]]
            fourth=freq[digits[3]]
            for i in range(len(first)):
                for j in range(len(second)):
                    for k in range(len(third)):
                        for l in range(len(fourth)):
                            ans.append(first[i]+second[j]+third[k]+fourth[l])
            return ans
        """
        :type digits: str
        :rtype: List[str]
        """
        