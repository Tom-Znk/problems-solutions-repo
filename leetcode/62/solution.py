class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Solution is a simple permutation problem, where out of (m+n)! choices we must make m down choices and n right choices. So, the final calculation is (m+n)! / (n!m!). However, consider that our grid is from 0,0 to m-1, n-1, so we have to "scale" both m and n before calculating.
        """

        m, n = m-1, n-1

        return int(factorial(m+n)/(factorial(m) * factorial(n)))
