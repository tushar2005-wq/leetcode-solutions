class Solution(object):
    def processStr(self, s):
        result_list=[]
        for i in s:
            if i.islower():
                result_list.append(i)
            elif i=="*" and result_list:
                result_list.pop()
            elif i=="#":
                result_list.extend(result_list[:])
            elif i=="%":
                result_list.reverse()
        s="".join(result_list)
        return s
        """
        :type s: str
        :rtype: str
        """
        