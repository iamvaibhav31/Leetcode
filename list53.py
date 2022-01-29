def maxSubArray(nums):
    """
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
    """
    maxsubarraysum = nums[0]
    currentsum = 0
    
    for n in nums:
        if currentsum < 0:
            currentsum = 0
            
        currentsum += n
        maxsubarraysum = max(maxsubarraysum , currentsum)
        
    return maxsubarraysum


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
