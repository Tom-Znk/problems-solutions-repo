class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        """Basically a DP approach"""


        tap_cover = [float('inf')] * (n + 1)
        tap_cover[0] = 0
        
        for i, r in enumerate(ranges):

            start, end = max(0, i - r), min(n, i + r)

            for j in range(start + 1, end + 1):
                
                tap_cover[j] = min(tap_cover[j], tap_cover[start] + 1)
                
        return tap_cover[-1] if tap_cover[-1] != float('inf') else -1
        