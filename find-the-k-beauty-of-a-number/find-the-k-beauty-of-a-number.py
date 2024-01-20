class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:


        stringnum  = str(num)

        count = 0

        for i in range(len(stringnum)-k+1):

            slide = stringnum[i:i+k]


            numslide  = int(slide)

            if  numslide!=0 and num%numslide==0:

                count+=1

        return count

        

