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
        
    dfs([], 1, k)
    return results

    # return list(itertools.combinations(range(1, n + 1), k))


# 리트코드 39번

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


# 리트코드 78번

def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


# 리트코드 332번

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a])
        route.append(a)

    dfs('JFK')
    return route[::-1]


# 리트코드 207번

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):

        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True