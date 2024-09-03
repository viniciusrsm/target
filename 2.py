def fib(n, comp):
    n1, n2, n3, c = 0, 1, 1, 1
    flag = False
    while c <= n:
        if n3 == comp or comp == 0:
            flag = True
            break
        c += 1
        n1, n2 = n2, n3
        n3 = n1 + n2
    print("Está presente na sequência") if flag else print("Não está presente na sequência")

compInp = int(input("Informe um número maior ou igual a 0:\n"))
fib(compInp+2, compInp)