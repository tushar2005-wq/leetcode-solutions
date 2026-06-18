class Solution(object):
    def angleClock(self, hour, minutes):
        hour_angle=(hour%12) *30 + minutes*0.5
        minutes_angle= minutes*6

        total_angle=abs(hour_angle-minutes_angle)
        return min(total_angle,360-total_angle)
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        