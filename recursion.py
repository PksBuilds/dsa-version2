class Solution:
    def printNumbers(self, n):
       
        if n == 0:
            return 
        self.printNumbers(n-1)
        print(n)
       
        


if __name__ == "__main__":
    sol = Solution()
    sol.printNumbers(9)