n, a, b = list(map(int, input().split()))
p = (10 ** 9) + 7

def powmod(x, exp, mod):
    if(exp == 1):
        return x % mod

    if(exp % 2 == 1):
        return (x * powmod(x, exp - 1, mod)) % mod

    x = powmod(x, exp / 2, mod)

    return (x * x) % mod

# nCrを計算するが、nもrも巨大なためフェルマーの小定理を利用する
# x = nPr
# y = r!
# x / y ≡ x * y^-1
# p を法とした時、掛けるたびにmodをとった数同士の割り算はうまくいかない
# フェルマーの小定理から
# y^(p-1) ≡ 1
# y * y^(p-2) ≡ 1
# y^(p-2)がyの逆元と同じ振る舞いをするのでy^(p-2)を掛ける
def combination(n, r, mod):
    x = 1
    y = 1

    for i in range(r):
        x *= n - i # n * (n - 1) * (n - 2) * ... * (n - i + 1)
        x %= mod
        y *= i + 1 # r * (r - 1) * (r - 2) * ... * 2 * 1 を逆さまにかけていく
        y %= mod

    return x * powmod(y, mod - 2, mod) % mod


total = powmod(2, n, p) - 1 #1本も花を選ばないパターンは除外する
comb_a = combination(n, a, p)
comb_b = combination(n, b, p)


print((total - comb_a - comb_b) % p)
