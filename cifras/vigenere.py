from ._base import A, _map


# vigenere(t, k, d=1) -> str
# Cifra de Vigenere: cifra polialfabetica (varias cifras de Cesar alternadas).
#
# Parametros:
#   t: texto a cifrar ou decifrar.
#   k: palavra-chave (ex: "CHAVE").
#   d: 1 cifra, -1 decifra.
#
# Funcionamento:
#   - A chave e repetida ao longo do texto: CHAVECHAVECHAVE...
#   - Cada letra e deslocada pelo valor da letra da chave na mesma posicao
#     (A=0, B=1, C=2...). Ex: texto T + chave C(2) -> V.
#   - O contador j (uma lista, para poder ser alterado dentro de f) so avanca
#     quando uma letra e processada; espacos nao consomem a chave.
#
# Seguranca: mais forte que Cesar, pois a mesma letra vira letras diferentes.
# Ainda assim e quebrada descobrindo o tamanho da chave (metodo de Kasiski) e
# aplicando analise de frequencia em cada posicao.
def vigenere(t, k, d=1):
    k, j = k.upper(), [0]

    def f(x, i):
        s = A.index(k[j[0] % len(k)]); j[0] += 1
        return x + d * s
    return "".join(_map(c, f) if c in A else c for c in t.upper())
