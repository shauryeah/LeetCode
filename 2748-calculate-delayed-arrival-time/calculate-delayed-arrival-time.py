class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        if (arrivalTime + delayedTime)>=24:
            return (arrivalTime + delayedTime)-24
        else:
            return arrivalTime + delayedTime