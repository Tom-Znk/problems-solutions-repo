class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        We can solve this problem via a dynamic programming approach. Create a matrix for number of ways to reach a target, with first row/column bein one (since we cannot make turns from those positions).
        """

        number_of_ways = [
                    [1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)
                ]

        for row in range(1, m):
            for column in range(1, n):
                number_of_ways[row][column] = number_of_ways[row][column - 1] + number_of_ways[row-1][column]

        return number_of_ways[m-1][n-1] 

