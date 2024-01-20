class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        j = len(digits)-1

        while(j>=0):

            if digits[j]<9:

                digits[j]+=1

                break

            else:

                digits[j] = 0

                if j == 0:

                    digits.insert(0,1)

            j-=1

        return digits

                    