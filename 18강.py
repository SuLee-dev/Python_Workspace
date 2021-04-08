# 리트코드 704번

def search(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    return -1


# 리트코드 33번

def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
        
    pivot = left

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1