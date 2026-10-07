from cifras import METODOS
m = "TRANSFERIR DOCUMENTO PARA SERVIDOR CENTRAL"
ks = ["3", "QWERTYUIOPASDFGHJKLZXCVBNM", "5,8", "CHAVE", "3,3,2,5", "ZEBRA", "segredo"]
for (n, f, _), k in zip(METODOS.values(), ks):
    c = f(m, k, 1); p = f(c, k, -1)
    ok = p.rstrip("X") == m.replace(" ", "") if n.startswith("Hill") else p == m
    print(f"{n:15} {'OK' if ok else 'FALHOU'} -> {c}")
