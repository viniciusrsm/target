fat = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

est = input("Escolha o estado que deseja consultar a porcentagem:\n0: SP\n1: RJ\n2: MG\n3: ES\n4: Outros\n")
print(fat[int(est)] / sum(fat))