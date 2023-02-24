def bs(nums,target)-> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if target == nums[mid]:
            return mid
        elif target==nums[start]:
            return start
        elif target==nums[end]:
            return end
        elif target < nums[mid]:
            end = int(mid - 1)
        else:
            start = int(mid + 1)

print(bs([-1,0,3,5,9,12], 9))