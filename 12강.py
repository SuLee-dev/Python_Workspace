# 리트코드 200번

def numIslands(self, grid: List[List[str]]) -> int:

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


# 리트코드 17번

def letterCombinations(self, digits: str) -> List[str]:

    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        
        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)
        
    if not digits:
        return []

    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
              '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    dfs(0, "")
    return result


# 리트코드 46번

def permute(self, nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

    # return list(map(list, itertools.permutations(nums)))


# 리트코드 77번

def combine(self, n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
        
    dfs([], 0, k)
    return results

    # return list(itertools.combinations(range(1, n + 1), k))