N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

mod_A = {key: 0 for key in range(46)}
mod_B = {key: 0 for key in range(46)}
mod_C = {key: 0 for key in range(46)}

for a in A:
    tmp = a % 46
    mod_A[tmp] += 1
for b in B:
    tmp = b % 46
    mod_B[tmp] += 1
for c in C:
    tmp = c % 46
    mod_C[tmp] += 1

ans = 0
for i in range(46):
    for j in range(46):
        ans += mod_A[i] * mod_B[j] * mod_C[(92-i-j) % 46]

print(ans)
