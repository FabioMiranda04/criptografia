import random


# fluxo(t, k, d=1) -> str
# Cifra de Fluxo (stream cipher) com XOR.
#
# Parametros:
#   t: ao cifrar, o texto original; ao decifrar, o texto cifrado em hex.
#   k: semente (ex: "segredo") que gera a sequencia pseudoaleatoria.
#   d: 1 cifra, -1 decifra.
#
# Funcionamento:
#   - random.Random(k) cria um gerador iniciado com a semente: a mesma
#     semente sempre gera a mesma sequencia de numeros (o keystream).
#   - O texto vira bytes (UTF-8) e cada byte e combinado com um byte do
#     keystream (0 a 255) usando XOR (^).
#   - Como (x ^ k) ^ k = x, aplicar o mesmo XOR de novo desfaz a cifra.
#   - Cifrar devolve hexadecimal (os bytes podem nao ser imprimiveis);
#     decifrar converte o hex de volta em bytes e depois em texto.
#
# Seguranca: apenas didatica. O modulo random (Mersenne Twister) NAO e
# criptograficamente seguro. Em uso real, use ChaCha20 ou AES-CTR, e nunca
# reutilize a mesma semente para mensagens diferentes.
def fluxo(t, k, d=1):
    rnd = random.Random(k)
    data = t.encode() if d == 1 else bytes.fromhex(t)
    out = bytes(b ^ rnd.randrange(256) for b in data)
    return out.hex() if d == 1 else out.decode()
