from cifras import METODOS

while True:
    print("\n=== Criptografia Classica ===")
    for n, (nome, _, _) in METODOS.items():
        print(f"{n} - {nome}")
    op = input("0 - Sair\n> ").strip()
    if op == "0": break
    if op not in METODOS: continue
    nome, f, dica = METODOS[op]
    d = 1 if input("1 - Cifrar / 2 - Decifrar: ").strip() != "2" else -1
    texto = input("Texto: ")
    chave = input(f"Chave {dica}: ")
    try:
        print("Resultado:", f(texto, chave, d))
    except Exception as e:
        print("Erro:", e)
