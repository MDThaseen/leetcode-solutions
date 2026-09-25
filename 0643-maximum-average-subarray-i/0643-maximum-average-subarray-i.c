double findMaxAverage(int* nums, int numsSize, int k) {
    int sum = 0;

    for (int i = 0; i < k; i++)
        sum += nums[i];

    int maxsum = sum;
    int start = 0;
    int end = k;

    while (end < numsSize) {
        sum -= nums[start];
        start++;

        sum += nums[end];
        end++;

        if (sum > maxsum)
            maxsum = sum;
    }

    return (double)maxsum / k;
}
