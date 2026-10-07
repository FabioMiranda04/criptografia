# Reune todas as cifras e o menu METODOS: numero -> (nome, funcao, dica da chave).
from .cesar import cesar
from .substituicao import substituicao
from .afim import afim
from .vigenere import vigenere
from .hill import hill
from .transposicao import transposicao
from .fluxo import fluxo

METODOS = {
    "1": ("Cesar", cesar, "deslocamento (ex: 3)"),
    "2": ("Substituicao", substituicao, "alfabeto de 26 letras (ex: QWERTYUIOPASDFGHJKLZXCVBNM)"),
    "3": ("Afim", afim, "a,b (ex: 5,8)"),
    "4": ("Vigenere", vigenere, "palavra (ex: CHAVE)"),
    "5": ("Hill 2x2", hill, "a,b,c,d (ex: 3,3,2,5)"),
    "6": ("Transposicao", transposicao, "palavra (ex: ZEBRA)"),
    "7": ("Cifra de Fluxo", fluxo, "semente (ex: segredo)"),
}
