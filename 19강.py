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


# 리트코드 393번

def validUtf8(self, data: List[int]) -> bool:
    def check(size):
        for i in (start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    start = 0
    while start < len(data):
        first = data[start]
        if (first >> 3) == 0b11110 and check(3):
            start += 4
        elif (first >> 4) == 0b1110 and check(2):
            start += 3
        elif (first >> 5) == 0b110 and check(1):
            start += 2
        elif (first >> 7) == 0:
            start += 1
        else:
            return False
    return True


# 리트코드 191번

def hammingWeight(self, n: int) -> int:

    count = 0
    while n:
        n &= n - 1
        count += 1
    return count