class Solution(object):
    def twoEditWords(self, queries, dictionary):
        final=[]
        k=0
        count=0
        for i in queries:
            for j in dictionary:
                diff=0
                for k in range(len(i)):
                    if i[k]!=j[k]:
                        diff+=1
                    if diff>2:
                        break
                if diff<=2:
                    final.append(i)
                    break
        return final
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        