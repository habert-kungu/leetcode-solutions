class Solution(object):
    def removeDuplicates(self, nums):
        numbers_set = set()
        counter = 0
        for i in range(len(nums)):
            if nums[i] not in numbers_set:
                numbers_set.add(nums[i])
                nums[counter] = nums[i]
                counter += 1
        return counter
