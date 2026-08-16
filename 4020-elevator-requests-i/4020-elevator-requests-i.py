class Solution(object):
    def elevatorRequests(self, n, requests):
        time=0
        floor=0
        i=0
        while i<len(requests):
            time+=abs(requests[i]-floor)
            floor=requests[i]
            i+=1
        return time
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        