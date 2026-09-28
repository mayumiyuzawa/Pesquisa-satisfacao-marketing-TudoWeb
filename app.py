print("=== PESQUISA DE SATISFAÇÃO - TUDOWEB ===")
excelente = 0
ruim = 0

for entrevistado in range(1, 51):

    print(f"\nEntrevistado {entrevistado}")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    print("\nQual é a sua opinião sobre o atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    # Verifica a opinião do entrevistado
    if opiniao == 1:
        excelente += 1
        print("Opinião registrada: EXCELENTE")
    elif opiniao == 2:
        print("Opinião registrada: BOM")
    elif opiniao == 3:
        ruim += 1
        print("Opinião registrada: RUIM")
    else:
        print("Opção inválida.")

# Resultado final da pesquisa
print("\n=== RESULTADO DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)