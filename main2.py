import os

infos = [{"nome": "Bruno", "idade": "18", "cidade": "Osasco"}]

def opcoes():
    opcao = int(input("Escolha uma opção: "))
    match opcao:
        case 1:
            infos = modificar_idade()
        case 2:
           mostrar_infos()

def voltar_menu():
    input("\nSelecione uma tecla para voltar ao menu principal: ")
    main()

def modificar_idade():
    item = input("Digite o novo valor da idade: ")
    dados_infos = [{"nome": "Bruno", "idade": item, "cidade": "Osasco"}]
    infos.append(dados_infos)
    voltar_menu()

def mostrar_infos():
    print(infos)
    voltar_menu()

def main():
    os.system("cls")
    opcoes()

main()