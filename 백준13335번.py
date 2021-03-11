# 1초마다 트럭의 위치를 업데이트하는 함수
def updateLocation(li_online, li_waiting, l):
    li_online.pop() # 마지막 좌표 제거
    for i in range(len(li_online)): # 한칸씩 옆으로 이동
        li_online[i][0] += 1
    li_online.insert(0, [0, 0]) # 처음 좌표 다시 생성

    if len(li_waiting) > 0:
        # 다리 위의 트럭 총 무게와 들어올 트럭의 무게의 합이 최대하중보다 낮을 시 트럭 추가
        if (sum(j for i, j in li_online) + li_waiting[0] <= l): 
            li_online[0][1] = li_waiting[0]
            li_waiting.remove(li_waiting[0])

n, w, l = map(int, input().split())
# n = 지나가려는 트럭의 수, w = 다리의 길이, l = 다리의 최대하중

truckWeight = list(map(int, input().split()))

# 다리 위 시작 위치 : 0 으로 설정

time = 0

# 각 좌표와 그 좌표에 있는 트럭의 무게의 리스트 생성
truckLocation = [[i, 0] for i in range(w)]


# 다리 위의 트럭이 남아 있지 않을 때까지 1초씩 증가
while True:
    time += 1
    updateLocation(truckLocation, truckWeight, l)
    if (sum (j for i, j in truckLocation) == 0):
        break

print(time)