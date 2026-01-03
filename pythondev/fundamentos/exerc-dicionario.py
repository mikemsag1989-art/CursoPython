import pprint

produto1 = input("Digite o nome do primeiro produto: \n")
preco1 = float(input("Digite o preço do primeiro produto: \n")) 
produto2 = input("Digite o nome do segundo produto: \n")
preco2 = float(input("Digite o preço do segundo produto: \n"))
produto3 = input("Digite o nome do terceiro produto: \n")
preco3 = float(input("Digite o preço do terceiro produto: \n"))

dicProdutos = {
    produto1: preco1,
    produto2: preco2,
    produto3: preco3
}

pp= pprint.PrettyPrinter(depth=4) # definindo a profundidade de exibição do dicionário
pp.pprint(dicProdutos)


# produto mais caro
maisCaro = max(dicProdutos, key=dicProdutos.get)
print(f"O produto mais caro é {maisCaro} que custa R$ {dicProdutos[maisCaro]:.2f}")

#media dos preços
mediaPrecos = sum(dicProdutos.values()) / len(dicProdutos)
print(f"A média dos preços é R$ {mediaPrecos:.2f}")


