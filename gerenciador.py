#Python

import json
import os

# Funções

def carregar_produtos():
    if os.path.exists("produtos.json"):
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            return json.load (arquivo)
    return []

produtos = carregar_produtos()
print (f"Produtos carregados: {len(produtos)} encontrado(s).")

def salvar_produtos():
    with open("produtos.json", "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def editar_produto():
    global produtos
    nome = input("Digite o nome do produto a editar: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(f"Produto atual: {produto['nome']} - R${produto['preco']} x {produto['quantidade']}")
            novo_preco = float(input("Novo preço: "),2)
            nova_quantidade = int(input("Nova quantidade: "))
            produto["preco"] = novo_preco
            produto["quantidade"] = nova_quantidade
            salvar_produtos()
            print(f"Produto '{nome}' atualizado com sucesso.")
            return
    print("Produto não encontrado.")

def mostrar_menu():
    print ("\n=== GERENCIADOR DE PRODUTOS ===")
    print ("1- Adicionar produto")
    print ("2- Listar produtos")
    print ("3- Remover produto")
    print ("4- Calcular valor total do estoque")
    print ("5- Editar produto")
    print ("6- Sair")

def calcular_total_estoque():
    total = 0
    for produto in produtos:
        total += produto["preco"] * produto["quantidade"]
    print(f"Valor total em estoque: R${total:.2f}")

def adicionar_produto():
    nome=input("Nome do Produto: ")
    preco=round(float(input("Preço: ")),2)
    quantidade=int(input("Quantidade: "))
    produto = {"nome":nome, "preco":preco, "quantidade":quantidade}
    produtos.append(produto)
    salvar_produtos()
    print (f"Produto '{nome}' adicionado com sucesso.")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado")
        return
    print("\n --- Produtos Cadastrados ---")
    for produto in produtos:
        print(f"{produto['nome']} - R${produto['preco']} x {produto['quantidade']}")

def remover_produto():
    nome = input("Digite o nome do produto a remover: ")
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            salvar_produtos()
            print(f"Produto '{nome}' removido.")
            return
    print("Produto não encontrado.")

# Programa principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        remover_produto()
    elif opcao == "4":
        calcular_total_estoque()
    elif opcao == "5":
        editar_produto()
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")