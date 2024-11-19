class Solution(object):
    def removeDuplicates(self, nums):
        numbers_set = set()
        # setcounter to maintain the new size of the Array
        counter = 0
        # loop thru the arr and compare the two numbers added
        # in the set and the one in the arr
        for i in range(len(nums)):
            if nums[i] not in numbers_set:
                numbers_set.add(nums[i])
                nums[counter] = nums[i]
                counter += 1
        return counter
