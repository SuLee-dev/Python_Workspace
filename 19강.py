# 리트코드 136번

def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num

    return result


# 리트코드 461번

def hammingDistance(self, x: int, y: int) -> int:

    return bin(x ^ y).count('1')


# 리트코드 371번

def getSum(self, a: int, b: int) -> int:

    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    if a > INT_MAX:
        a = ~(a ^ MASK)

    return a