# Modulo base compartilhado por todas as cifras classicas.
#
# A: alfabeto de referencia (26 letras maiusculas). Cada letra e tratada pelo
#    seu indice: A=0, B=1, ..., Z=25. Toda a aritmetica das cifras e mod 26.
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# _map(t, f) -> str
# Funcao auxiliar que percorre o texto letra a letra e aplica uma transformacao.
#
# Parametros:
#   t: texto de entrada (convertido para maiusculas).
#   f: funcao f(x, i) que recebe o indice da letra no alfabeto (x) e a posicao
#      dela no texto (i), e devolve o novo indice.
#
# Funcionamento:
#   - Para cada letra calcula f(x, i) % 26 e pega a letra correspondente em A
#     (o % 26 faz o alfabeto "dar a volta": depois de Z vem A).
#   - Caracteres que nao sao letras (espacos, numeros, pontuacao) ficam iguais.
#
# Exemplo: _map("ABC", lambda x, i: x + 1) -> "BCD"
def _map(t, f):
    return "".join(A[f(A.index(c), i) % 26] if c in A else c for i, c in enumerate(t.upper()))
