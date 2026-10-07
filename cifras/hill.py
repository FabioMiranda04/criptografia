from ._base import A


# hill(t, k, d=1) -> str
# Cifra de Hill 2x2: baseada em algebra linear (multiplicacao de matrizes).
#
# Parametros:
#   t: texto a cifrar ou decifrar (so as letras sao usadas; espacos somem).
#   k: matriz-chave 2x2 no formato "a,b,c,e", que representa:
#          | a  b |
#          | c  e |
#   d: 1 cifra, -1 decifra.
#
# Funcionamento:
#   - O texto e dividido em pares de letras (x1, x2), e cada par e
#     multiplicado pela matriz:
#         y1 = (a*x1 + b*x2) mod 26
#         y2 = (c*x1 + e*x2) mod 26
#   - Para decifrar usa a matriz inversa mod 26:
#         inv(det) * |  e  -b |     com det = a*e - b*c
#                    | -c   a |
#   - Se o numero de letras for impar, adiciona X (indice 23) no fim.
#
# Restricao: o determinante precisa ser coprimo de 26, senao nao ha inversa.
#
# Seguranca: esconde a frequencia de letras isoladas, mas cai com ataque de
# texto conhecido (alguns pares claro/cifrado revelam a matriz).
def hill(t, k, d=1):
    a, b, c, e = map(int, k.split(","))
    if d == -1:
        inv = pow(a * e - b * c, -1, 26)
        a, b, c, e = e * inv, -b * inv, -c * inv, a * inv
    s = [A.index(x) for x in t.upper() if x in A]
    if len(s) % 2: s.append(23)  # pad X
    return "".join(A[(a*s[i] + b*s[i+1]) % 26] + A[(c*s[i] + e*s[i+1]) % 26] for i in range(0, len(s), 2))
