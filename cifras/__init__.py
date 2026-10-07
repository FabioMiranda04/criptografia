import random
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _map(t, f):
    return "".join(A[f(A.index(c), i) % 26] if c in A else c for i, c in enumerate(t.upper()))

def cesar(t, k, d=1):
    return _map(t, lambda x, i: x + d * int(k))

def substituicao(t, k, d=1):
    k = k.upper()
    return "".join((k[A.index(c)] if d == 1 else A[k.index(c)]) if c in A else c for c in t.upper())

def afim(t, k, d=1):
    a, b = map(int, k.split(","))
    inv = pow(a, -1, 26)
    return _map(t, lambda x, i: a * x + b if d == 1 else inv * (x - b))

def vigenere(t, k, d=1):
    k, j = k.upper(), [0]
    def f(x, i):
        s = A.index(k[j[0] % len(k)]); j[0] += 1
        return x + d * s
    return "".join(_map(c, f) if c in A else c for c in t.upper())

def hill(t, k, d=1):  # chave 2x2 "a,b,c,e"
    a, b, c, e = map(int, k.split(","))
    if d == -1:
        inv = pow(a * e - b * c, -1, 26)
        a, b, c, e = e * inv, -b * inv, -c * inv, a * inv
    s = [A.index(x) for x in t.upper() if x in A]
    if len(s) % 2: s.append(23)  # pad X
    return "".join(A[(a*s[i] + b*s[i+1]) % 26] + A[(c*s[i] + e*s[i+1]) % 26] for i in range(0, len(s), 2))

def transposicao(t, k, d=1):  # transposicao colunar, chave = palavra
    o = sorted(range(len(k)), key=lambda i: k[i]); n = len(k)
    if d == 1:
        return "".join(t[i::n] for i in o)
    cols, p, r = {}, 0, [0] * len(t)
    for i in o:
        l = len(range(i, len(t), n)); cols[i] = t[p:p+l]; p += l
    for i in range(n):
        r[i::n] = cols[i]
    return "".join(r)

def fluxo(t, k, d=1):  # XOR com keystream gerado pela semente; saida em hex
    rnd = random.Random(k)
    data = t.encode() if d == 1 else bytes.fromhex(t)
    out = bytes(b ^ rnd.randrange(256) for b in data)
    return out.hex() if d == 1 else out.decode()

METODOS = {
    "1": ("Cesar", cesar, "deslocamento (ex: 3)"),
    "2": ("Substituicao", substituicao, "alfabeto de 26 letras (ex: QWERTYUIOPASDFGHJKLZXCVBNM)"),
    "3": ("Afim", afim, "a,b (ex: 5,8)"),
    "4": ("Vigenere", vigenere, "palavra (ex: CHAVE)"),
    "5": ("Hill 2x2", hill, "a,b,c,d (ex: 3,3,2,5)"),
    "6": ("Transposicao", transposicao, "palavra (ex: ZEBRA)"),
    "7": ("Cifra de Fluxo", fluxo, "semente (ex: segredo)"),
}
