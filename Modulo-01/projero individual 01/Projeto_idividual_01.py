# Lista gem de candidatos preconfigurados, para conseguir realizar a consulta
candidatos = [
    ('Vitor','e5_t6_p8_s8'),
    ('Manoel','e4_t3_p7_s8'),
    ('Carlos','e5_t3_p8_s8'),
    ('José','e10_t7_p7_s8'),
    ('Davi','e5_t4_p8_s9'),
    ('Marlon','e5_t2_p6_s5'),
    ('Marcos','e8_t5_p4_s9'),
    ('Marcela','e5_t7_p5_s1'),
    ('Alex','e1_t5_p8_s9')
]

def inserir_novo_candidato():   #Definicndo a função para inserir novos candidados na memoria
    
    nome = input("Digite o nome do candidato: ")
    e = input("Digite a nota de entrevista: ")
    t = input("Digite a nota do teste teórico: ")
    p = input("Digite a nota do teste prático: ")
    s = input("Digite a nota de soft skills: ")
    candidatos.append((nome, f"e{e}_t{t}_p{p}_s{s}"))

def consultar_candidatos():     #Definido a função para imprimir os novos candidatos
    
    print("Lista de candidatos e suas notas:")
    for candidato, notas in candidatos:
        print(f"{candidato}: {notas}")

def achar_candidato_por_notas():    #Realizando a função para encontra os candidatos desejados.
    """Função para encontrar candidatos com notas acima de um certo limiar."""
    nota_e = int(input('Digite a nota mínima de entrevista: '))
    nota_t = int(input('Digite a nota mínima do teste teórico: '))
    nota_p = int(input('Digite a nota mínima do teste prático: '))
    nota_s = int(input('Digite a nota mínima de soft skills: '))

    candidatos_aprovados = []
    for candidato, notas in candidatos:
        notas_dict = converter_notas(notas)
        if (notas_dict['e'] >= nota_e and notas_dict['t'] >= nota_t and
            notas_dict['p'] >= nota_p and notas_dict['s'] >= nota_s):
            candidatos_aprovados.append(candidato)

    if candidatos_aprovados:
        print("Candidatos aprovados:")
        for candidato in candidatos_aprovados:
            print(candidato)
    else:
        print("Nenhum candidato atende aos critérios.")

def converter_notas(nota_str):
    """Função para converter uma string de notas em um dicionário."""
    notas_dict = {}
    notas_str_split = nota_str.split('_')
    for item in notas_str_split:
        notas_dict[item[0]] = int(item[1:])
    return notas_dict

# Loop principal para interação com o usuário
while True:
    print("\nBem-vindo ao processo de seleção por notas. O que você deseja?")
    print("1 - Inserir um novo candidato")
    print("2 - Consultar a lista de candidatos")
    print("3 - Consultar candidatos aprovados")
    print("4 - Fechar o programa")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_novo_candidato()
    elif opcao == '2':
        consultar_candidatos()
    elif opcao == '3':
        achar_candidato_por_notas()
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

