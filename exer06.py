while True:
    n1 =float(input("digite n1:"))
    while n1<0 or n1>10:
        n1=float(input("valor ivalido,digite n1 novamente:"))
    n2 =float(input("digite n2:"))
    while n2<0 or n2>10:
        n2=float(input("valor ivalido,digite n2 novamente:"))
    media=(n1+n2)/2
    print(media)
    resposta=input("deseja realizar outro calculo?")
    if resposta == "n":
        break