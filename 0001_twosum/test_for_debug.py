# class Solution:
#     def TwoSum(self,nums,target):
#         '''
#             num: list
#             target: int
#             out: list
#         '''
#         for i in range(len(nums)-1):
#             if ((target-nums[i]) in nums[i+1:]):
#                 return [i,nums.index(target-nums[i],i+1)]

class Solution:
    def TwoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                return [dict[target-nums[i]],i]
            if nums[i] not in dict.keys() :
                dict[nums[i]] = i


# test case
ins = Solution()
out1 = ins.TwoSum([2,11,7,7],9)
out2 = ins.TwoSum([3,2,3,4,3],6)
out3 = ins.TwoSum([-5,-5,11,4],6)
out4 = ins.TwoSum([3,2,4],6)
out5 = ins.TwoSum([3,3],6)
print("#############################")
print(out1,out2,out3,out4,out5)