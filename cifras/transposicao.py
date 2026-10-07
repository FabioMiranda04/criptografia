# transposicao(t, k, d=1) -> str
# Cifra de Transposicao Colunar: nao troca as letras, so muda a ordem delas.
#
# Parametros:
#   t: texto a cifrar ou decifrar (todos os caracteres sao mantidos,
#      inclusive espacos).
#   k: palavra-chave (ex: "ZEBRA"); o tamanho dela e o numero de colunas.
#   d: 1 cifra, -1 decifra.
#
# Funcionamento:
#   - o: ordem de leitura das colunas, obtida ordenando as letras da chave.
#     Para "ZEBRA": A(4), B(2), E(1), R(3), Z(0) -> colunas 4, 2, 1, 3, 0.
#   - Cifrar: o texto e escrito em linhas de n colunas; t[i::n] pega a
#     coluna i. As colunas sao concatenadas na ordem o.
#   - Decifrar: calcula o tamanho de cada coluna, recorta o texto cifrado na
#     mesma ordem (cols) e devolve cada coluna a sua posicao original
#     (r[i::n] = cols[i]), reconstruindo as linhas.
#
# Seguranca: a frequencia das letras e igual a do texto original, o que
# denuncia a transposicao. Historicamente era combinada com substituicao.
def transposicao(t, k, d=1):
    o = sorted(range(len(k)), key=lambda i: k[i]); n = len(k)
    if d == 1:
        return "".join(t[i::n] for i in o)
    cols, p, r = {}, 0, [0] * len(t)
    for i in o:
        l = len(range(i, len(t), n)); cols[i] = t[p:p+l]; p += l
    for i in range(n):
        r[i::n] = cols[i]
    return "".join(r)
