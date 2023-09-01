class Solution:
    def countBits(self, n: int) -> List[int]:

        """
        Just a DP solution. The pattern is 0112 1223 etc.
        """

        if n == 0:
            return [0]
        
        if n == 1:
            return [0, 1]

        result = [0] * (n+1)
        result[0], result[1] = 0, 1
    
        for i in range (2, n+1):
            if i%2 == 0:
                result[i] = result[i//2]
            else:
                result[i] = result[i//2] + 1

        return result

            