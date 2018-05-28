# -*- coding: UTF-8 -*-
def cadastrar(nomes):
    print "Digite o nome: "
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print "Qual nome voce gostaria de remover?"
    nome = raw_input()
    nomes.remove(nome)

def listar(nomes):
    print "Lista de nomes: "
    for nome in nomes:
        print nome

def menu():
    nomes = []
    opcao = ""
    while(opcao != "0"):
        print "1 - Cadastrar\n2 - Remover\n3 - Listar\n4 - Alterar Nome\n0 - Sair\n\nDigite a opcao desejada: "
        opcao = raw_input()
        if(opcao == "1"):
            cadastrar(nomes)
        elif(opcao == "2"):
            remover(nomes)
        elif(opcao == "3"):
            listar(nomes)
        elif(opcao == "4"):
            alterar(nomes)
        else:
            print "Opcao invalida\n"

def alterar(nomes):
    print "Qual nome deseja alterar?"
    nome = raw_input()

    if(nome in nomes):
        indice = nomes.index(nome)
        nomes[indice] = raw_input("Informe o novo nome: ")
    else:
        print "Nome não se encontra na lista"

menu()
