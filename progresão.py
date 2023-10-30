primeiro_termo = int(input("digite o primeiro termo da sua PA:"))
razao = int(input("digite a razão da PA"))

termos_pa = []

for i in range(10):
    termo = primeiro_termo + i * razao
    termos_pa.append(termo)
    print(" os 10 primeiros termos da PA são")
    for termo in termos_pa:
     print(termo)