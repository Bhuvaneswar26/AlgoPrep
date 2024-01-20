class Solution(object):
    def threeSum(self, nums):

        length = len(nums)
        
        nums.sort()

        result = set()

        for i in range(length-2):


            j  = i+1

            k  =  length-1

            while(j<k):

                su = nums[i] + nums[j] +nums[k]

                if su == 0:

                    result.add((nums[i],nums[j],nums[k]))

                    j+=1

                    k-=1

                elif su<0:

                    j+=1
            
                else:

                    k-=1

        return list(result)
