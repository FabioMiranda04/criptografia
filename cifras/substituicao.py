from ._base import A


# substituicao(t, k, d=1) -> str
# Cifra de Substituicao Monoalfabetica.
#
# Parametros:
#   t: texto a cifrar ou decifrar.
#   k: alfabeto-chave com as 26 letras embaralhadas, sem repetir
#      (ex: "QWERTYUIOPASDFGHJKLZXCVBNM").
#   d: 1 cifra, -1 decifra.
#
# Funcionamento:
#   - Cifrar: a letra na posicao i do alfabeto normal vira a letra na posicao
#     i da chave. Com a chave acima: A->Q, B->W, C->E...
#   - Decifrar: procura a letra na chave e devolve a letra de mesma posicao
#     no alfabeto normal.
#   - Caracteres que nao sao letras sao mantidos.
#
# Seguranca: existem 26! (~4x10^26) chaves, o que impede forca bruta, mas a
# cifra cai com analise de frequencia (A e E sao as letras mais comuns em
# portugues).
def substituicao(t, k, d=1):
    k = k.upper()
    return "".join((k[A.index(c)] if d == 1 else A[k.index(c)]) if c in A else c for c in t.upper())
