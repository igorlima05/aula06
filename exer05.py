pin = 123456
tentativas = 1
resposta="excesso de tentativas, conta bloqueada"
while tentativas <= 3:
    senha = int(input("digite seu login:"))
    if senha == pin:
        resposta("login efetruado com sucesso")
        break
tentativas += 1
print(resposta)
