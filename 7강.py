# 리트코드 1번

def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 리트코드 42번

def trap(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:

            top = stack.pop()

            if not len(stack):
                continue

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume


# 리트코드 15번

def threeSum(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        sum = nums[i] + nums[left] + nums[right]
        while left < right:
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


# 리트코드 561번

def arrayPairSum(self, nums: List[int]) -> int:

    return sum(sorted(nums)[::2])


# 리트코드 238번

def productExceptSelf(self, nums: List[int]) -> List[int]:

    out = []
    p = 1
    for i in range(0, len(nums)):
        out.append(i)
        p = p * nums[i]

    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out


# 리트코드 121번

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxSize

    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price - min_price)

    return profit