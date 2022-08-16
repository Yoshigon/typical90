def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


MOD = 10 ** 9+7  # 出力の制限
N = 10 ** 5
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % MOD)
    inverse.append((-inverse[MOD % i] * (MOD//i)) % MOD)
    g2.append((g2[-1] * inverse[-1]) % MOD)

N = int(input())
#  N個のボールから、差がk以上になるように選ぶ選び方は、N-(a-1)(k-1) C a通りである。
for k in range(1, N+1):
    tmp = 0
    a = 1
    while N - (a-1) * (k-1) >= a:
        tmp += cmb(N - (a-1) * (k-1), a, MOD)
        tmp %= MOD
        a += 1
    print(tmp)
