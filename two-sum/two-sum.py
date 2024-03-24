class Solution:
    def twoSum(self, nums, target):

        for i in range(len(nums)):

            nums[i] = (nums[i],i)

        nums.sort()

        i = 0

        j = len(nums)-1

        while(True):

            if nums[i][0]+nums[j][0]>target:

                j-=1

            elif nums[i][0]+nums[j][0]<target:

                i+=1

            else:

                return (nums[i][1],nums[j][1])

        

            