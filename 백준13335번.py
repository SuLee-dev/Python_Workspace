n, w, l = map(int, input().split())
# n = 지나가려는 트럭의 수, w = 다리의 길이, l = 다리의 최대하중

truck = list(map(int, input().split()))
cnt = 0

# 다리 위 시작 위치 : 0, 다리 끝 도착 위치 : w
# 1초마다 트럭의 위치 파악
time = 0
truckOnLine = {}

# 각 좌표와 그 좌표에 있는 트럭의 무게의 딕셔너리 생성
for i in range(w + 1):
    truckOnLine[i] = 0

while True:
    time += 1
    if (sum(truckOnLine.values()) + truck[0] <= l and len(truckOnLine) < w):
        print()