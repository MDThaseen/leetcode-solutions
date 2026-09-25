/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function findMaxAverage(nums, k) {
    let currentSum = 0;

    // sum of first k elements
    for (let i = 0; i < k; i++) {
        currentSum += nums[i];
    }

    let maxSum = currentSum;

    // sliding window
    for (let i = k; i < nums.length; i++) {
        currentSum -= nums[i - k];
        currentSum += nums[i];

        maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum / k;
}
