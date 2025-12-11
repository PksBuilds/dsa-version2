class Solution:
     day=int(input("Enter a number between 1-7: "))
     def whichweekDay(self,day):
          
          match day:
               
                case 1:
                        return "Monday"
                case 2:
                        return "Tuesday"
                case 3:
                        return "Wednesday"
                case 4:
                        return "Thursday"
                case 5:
                        return "Friday"
                case 6:
                        return "Saturday"
                case 7:
                        return "Sunday"
                case _:
                        return "Invalid Day"
        
        
if __name__ == "__main__":
 sol = Solution()
print(sol.whichweekDay(sol.day))
            
pass
      

                 