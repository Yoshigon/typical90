N = int(input())
A, B, C = sorted(map(int, input().split()), reverse=True)
ans = 10000

for a in range(N // A, -1, -1):
    for b in range((N - A * a) // B, -1, -1):
        if (N - (A * a + B * b)) % C == 0:
            c = (N - (A * a + B * b)) // C
            ans = min(ans, a+b+c)

print(ans)
