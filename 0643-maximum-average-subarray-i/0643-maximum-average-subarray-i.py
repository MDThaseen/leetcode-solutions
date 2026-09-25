class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum -= nums[i - k]
            current_sum += nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum / k
