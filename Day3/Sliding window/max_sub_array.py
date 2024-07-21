arr1 = [1, 2, 3, 4, 5, 6]

def max_sub_array(nums, k):
    window_sum = sum(nums[0:k])
    max_av = window_sum/k

    for end in range(k, len(nums)):
        window_sum = window_sum + nums[end] - nums[end-k]
        max_av = max(max_av, window_sum/k)

    return max_av

print(max_sub_array(arr1, 3))