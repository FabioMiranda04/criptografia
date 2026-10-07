from ._base import _map


# cesar(t, k, d=1) -> str
# Cifra de Cesar: uma das cifras mais antigas, usada por Julio Cesar.
#
# Parametros:
#   t: texto a cifrar ou decifrar.
#   k: deslocamento (inteiro, pode vir como string, ex: "3").
#   d: direcao -> 1 cifra (soma k), -1 decifra (subtrai k).
#
# Funcionamento:
#   Cada letra e deslocada k posicoes no alfabeto: com k=3, A->D, B->E, Z->C.
#   Para decifrar basta deslocar no sentido contrario.
#
# Seguranca: muito fraca. So existem 25 chaves uteis, entao e quebrada por
# forca bruta (testando todas) ou por analise de frequencia.
#
# Exemplo: cesar("ABC", "3") -> "DEF"; cesar("DEF", "3", -1) -> "ABC"
def cesar(t, k, d=1):
    return _map(t, lambda x, i: x + d * int(k))
