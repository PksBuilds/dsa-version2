class Solution:
    def NnumbersSum(self, N):
        if N==0:
            return 0
        return N+self.NnumbersSum(N-1)
    print(NnumbersSum)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.NnumbersSum(100))
    pass

        