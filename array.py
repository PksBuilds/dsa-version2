class Solution:
    def findlength(self,s):

        return len(s)
    
if __name__ == "__main__":
 sol = Solution()
 k="hello world"
 print(sol.findlength(k))
 pass

class solution:
   def Accesschar(self,k):
      for i in range(len(k)):

        print(k[i])

if __name__ == "__main__":
    sol = solution()
    m="hello string"
    print(sol.Accesschar(m))
    pass

class solution2:
   def modify_string(self,k):
      new_str =k
      new_str += "world"

      return new_str
   
if __name__ == "__main__":
       sol = solution2()
       og= "hello"
       result= sol.modify_string(og)
       print("og", og)
       print("returned", result)
       pass
   
         