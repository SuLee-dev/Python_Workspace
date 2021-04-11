# 리트코드 136번

def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num

    return result


# 리트코드 461번

def hammingDistance(self, x: int, y: int) -> int:

    return bin(x ^ y).count('1')