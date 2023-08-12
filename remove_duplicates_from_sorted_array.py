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
        print(returnList)
        return len(returnList)