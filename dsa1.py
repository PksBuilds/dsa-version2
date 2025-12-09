class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            return "Grade A"
        elif marks >= 70:
            return "Grade B"
        elif marks >= 50:
            return "Grade C"
        elif marks >= 35:
            return "Grade D"
        else:
            return "Fail"

if __name__ == "__main__":
    # 1. Create the object
    solution = Solution()
    
    # 2. Read the number from input.txt (Does NOT print it)
    marks = int(input())
    
    # 3. Calculate and Print ONLY the grade
    print(solution.studentGrade(marks))