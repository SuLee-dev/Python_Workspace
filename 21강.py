# 리트코드 122번

def maxProfit(self, prices: List[int]) -> int:

    return sum(max(prices[i + 1] - prices[i], 0) for i in range(0, len(prices) - 1))


# 리트코드 406번

def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    heap = []
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    
    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], (-person[0], person[1]))
    return result


# 리트코드 621번

def leastInterval(self, tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        for task, _ in counter.most_common(n + 1):
            result += 1
            sub_count += 1

            counter.subtract(task)
            counter += collections.Counter()
        
        if not counter:
            break
        
        result += (n + 1) - sub_count
    
    return result


# 리트코드 134번

def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0

    for i in range(len(gas)):
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    
    return start


# 리트코드 455번

def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    result = 0
    for i in s:
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    
    return result