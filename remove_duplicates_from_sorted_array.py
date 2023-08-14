class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        returnList = []
        for x in nums:
            if x not in returnList:
                returnList.append(x)
        del nums[:]
        for i in returnList:
            nums.append(i)

        return len(nums)


sample = Solution()
test1 = [1,1,2]
test2 = [0,0,1,1,1,2,2,3,3,4]

sample.removeDuplicates(test1)
sample.removeDuplicates(test2)