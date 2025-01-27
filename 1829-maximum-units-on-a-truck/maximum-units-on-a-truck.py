class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
    
        max_units = 0
    
        for numberOfBoxes, unitsPerBox in boxTypes:
            if truckSize >= numberOfBoxes:
                max_units += numberOfBoxes * unitsPerBox
                truckSize -= numberOfBoxes
            else:
                max_units += truckSize * unitsPerBox
                break 
    
        return max_units