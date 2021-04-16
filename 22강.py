# 리트코드 169번

def majorityElement(self, nums: List[int]) -> int:

    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = self.majorityElement(nums[:half])
    b = self.majorityElement(nums[half:])

    return [b, a][nums.count(a) > half]


# 리트코드 241번

def diffWaysToCompute(self, input: str) -> List[int]:
    def compute(left, right, op):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + op + str(r)))
        return result

    if input.isdigit():
        return [int(input)]

    result = []
    for index, value in enumerate(input):
        if value in '+-*':
            left = self.diffWaysToCompute(input[:index])
            right = self.diffWaysToCompute(input[index + 1:])
            result.extend(compute(left, right, value))

    return result