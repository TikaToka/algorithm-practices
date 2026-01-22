h, m = map(int, input().split())
req = int(input())
reqH = req // 60
reqM = req % 60

over = 1 if (m + reqM) >= 60 else 0

resH = (h + reqH + over) % 24
resM = (m + reqM) % 60

print(resH, resM)
