import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int,input().split()))

dp = [0]* 100

dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(dp[N-1])

