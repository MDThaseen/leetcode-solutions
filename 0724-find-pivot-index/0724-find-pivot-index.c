int pivotIndex(int* nums, int n) {
    int total = 0;
    int leftSum =  0;
    int i;

    for (i=0; i<n; i++){
        total += nums[i];
    }

    for (i=0 ; i<n ; i++){
        int rightSum = total - nums[i] - leftSum;
        if (rightSum == leftSum){
            return i;
        }
        leftSum += nums[i];
    }
    return -1;
}