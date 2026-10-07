from ._base import _map


# afim(t, k, d=1) -> str
# Cifra Afim: combina multiplicacao e deslocamento.
#
# Parametros:
#   t: texto a cifrar ou decifrar.
#   k: chave no formato "a,b" (ex: "5,8").
#   d: 1 cifra, -1 decifra.
#
# Funcionamento:
#   - Cifrar:   E(x) = (a * x + b) mod 26
#   - Decifrar: D(x) = a^-1 * (x - b) mod 26
#   onde a^-1 e o inverso modular de a (numero que multiplicado por a da 1
#   em mod 26), calculado com pow(a, -1, 26).
#
# Restricao: a precisa ser coprimo de 26 (1, 3, 5, 7, 9, 11, 15, 17, 19, 21,
# 23, 25); senao o inverso nao existe e pow gera erro.
# Observacao: com a=1 vira uma cifra de Cesar com deslocamento b.
#
# Exemplo com k="5,8": A(0) -> 5*0+8 = 8 -> I
def afim(t, k, d=1):
    a, b = map(int, k.split(","))
    inv = pow(a, -1, 26)
    return _map(t, lambda x, i: a * x + b if d == 1 else inv * (x - b))
