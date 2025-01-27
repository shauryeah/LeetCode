class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        L=list(coordinates)
        if L[0] in ['a','c','e','g']:
            if L[1] in ['2','4','6','8']:
                return True
            else:
                return False
        else:
            if L[1] in ['2','4','6','8']:
                return False
            else:
                return True