class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        curr_mass=mass
        n=len(asteroids)
        for i in range(n):
            if curr_mass>=asteroids[i]:
                curr_mass+=asteroids[i]
            else:
                return False
        return True
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        