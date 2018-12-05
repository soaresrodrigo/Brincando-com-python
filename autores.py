import os
import subprocess



author = [
    ['code'],
    ['name'],
    ['lastname']
]

def main():    
    showMenu()
    opcao = input("Escolha a opção: ")
    
    if(opcao == '1'):
        createAuthor()
    elif(opcao == '2'):
        print("Pesquisar")
    elif(opcao == '3'):
        print("Visualizar todos")
    elif(opcao == '4'):
        print("Remover")
    elif(opcao == '5'):
        print("Obrigado por usar meu sistema")
    else:
        os.system('clear')
        print("Opção inválida, tente novamente...")
        input()
        return main()


def showMenu():
    os.system('clear')
    print("[----- Registro de autores -----]\n");
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Visualizar todos")
    print("4 - Remover")
    print("5 - Sair\n")

def createAuthor():
    print(author)

main()