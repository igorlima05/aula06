alunos = int(input("digite a quantidade de alunos de uma sala:"))
i = 1
soma=0
while i <= alunos:
    notas = int(input("digite as notas dos alunos:"))
    i = i + 1
    soma=soma+notas
media=soma/alunos
print(media)