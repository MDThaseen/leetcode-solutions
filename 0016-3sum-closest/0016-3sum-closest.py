class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()

        resultSum = nums[0] + nums[1] + nums[2]
        minDif = float('inf')

        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total == target:
                    return target

                diff = abs(total - target)

                if diff < minDif:
                    resultSum = total
                    minDif = diff

                if total < target:
                    l += 1
                else:
                    r -= 1

        return resultSum