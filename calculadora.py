

def Calcular(nvitorias, nderrotas):
    saldo = nvitorias - nderrotas
    if (nvitorias <= 10) :
        nivel = "Ferro"
    if (nvitorias >=11 and nvitorias <= 20):
        nivel = "Bronze"
    if (nvitorias >=21 and nvitorias <= 50):
        nivel = "Prata"
    if (nvitorias >=51 and nvitorias <= 80):
        nivel = "Ouro"
    if (nvitorias >=81 and nvitorias <= 90):
        nivel = "Diamante"
    if (nvitorias >=91 and nvitorias <= 100):
        nivel = "Lendario"
    if (nvitorias >=101):
        nivel = "Imortal"
    print(f"O Herói tem de saldo {saldo} está no nível de {nivel}")
    return nvitorias, nderrotas, saldo, nivel

Calcular(nvitorias=int(input("Insira o numero de vitorias: ")), nderrotas=int(input("Insira o numero de derrotas: ")))