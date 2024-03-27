def max_non_increasing_subsequence(arr):
    n = len(arr)
    dp = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] <= arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    max_length = max(dp)
    subsequence = []
    curr_len = max_length
    for i in range(n-1, -1, -1):
        if dp[i] == curr_len:
            subsequence.append(arr[i])
            curr_len -= 1
            if curr_len == 0:
                break
    
    return subsequence[::-1]

arr = [1, 3, 5, 4, 7, 6, 8, 9]
result = max_non_increasing_subsequence(arr)
print(result) 
