class Solution(object):
    def addDigits(self, num):
        while len(str(num))>1:
            temp=0
            for digit in str(num):
                temp+=int(digit)
            num=temp
        return num
            
        """
        :type num: int
        :rtype: int
        """
        