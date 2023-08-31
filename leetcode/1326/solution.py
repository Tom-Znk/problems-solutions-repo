class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        """
        Basically a standard DP approach
        LINK : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/
        """


        tap_cover = [float('inf')] * (n + 1)
        tap_cover[0] = 0
        
        for i, tap_diameter in enumerate(ranges):

            start, end = max(0, i - tap_diameter), min(n, i + tap_diameter)

            for j in range(start + 1, end + 1):
                
                tap_cover[j] = min(tap_cover[j], tap_cover[start] + 1)
                
        return tap_cover[-1] if tap_cover[-1] != float('inf') else -1
        