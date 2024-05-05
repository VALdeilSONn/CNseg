import csv
import datetime
import os

class Questionario:
    def __init__(self):
        self.respostas = []
        self.perguntas = [
            "Você já realizou algum tipo de investimento? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Sabe como funciona o mundo de investimentos em Cripto? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Você considera as Criptomoedas um investimento seguro? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Você possui algum fundo de emergência? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Você conhece alguém que realiza algum tipo de investimento incluindo as Criptomoedas? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Você arriscaria a iniciar no mercado de investimentos? (1 - Sim, 2 - Não, 3 - Não sei): "
        ]
        self.criar_csv()

    def criar_csv(self, Documentos='questionario.csv'):
        caminho_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')
        if not os.path.exists(caminho_documentos):
            os.makedirs(caminho_documentos)
        nome_arquivo = os.path.join(caminho_documentos, Documentos)
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Idade", "Genero", "Data/Hora", "Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4", "Resposta 5", "Resposta 6"])

    def coletar_informacoes(self):
        while True:
            try:
                idade = int(input("Digite sua idade (00 para encerrar): "))
                if idade == 0:
                    return False
                elif idade < 0:
                    print("A idade deve ser um número positivo.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido para a idade.")
        genero = input("Digite seu gênero (M/F): ").upper()
        while genero not in ['M', 'F']:
            print("Opção inválida. Por favor, digite M ou F.")
            genero = input("Digite seu gênero (M/F): ").upper()
        self.inserir_resposta(idade, genero)
        return True

    def inserir_resposta(self, idade, genero):
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        respostas = [idade, genero, data_hora]
        for pergunta in self.perguntas:
            resposta = input(pergunta)
            while resposta not in ['1', '2', '3']:
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")
                resposta = input(pergunta)
            respostas.append(resposta)
        self.respostas.append(respostas)

    def escrever_csv(self, Documentos='questionario.csv'):
        caminho_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')
        nome_arquivo = os.path.join(caminho_documentos, Documentos)
        with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerows(self.respostas)
        print(f"Dados adicionados ao arquivo CSV {nome_arquivo}")

    def exibir_resultados(self):
        # Criação dos cabeçalhos das colunas
        cabecalhos = ['Idade', 'Gênero', 'Data/Hora', 'Resposta_1', 'Resposta_2', 'Resposta_3', 'Resposta_4', 'Resposta_5', 'Resposta_6']
        
        # Método para exibir os resultados do questionário de forma mais legível
        print("Resultados do Questionário:")
        
        # Imprime linha horizontal para separar cabeçalhos das colunas
        print("+" + "-" * 8 + "+" + "-" * 8 + "+" + "-" * 19 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")
        
        # Imprime os cabeçalhos das colunas
        print("|{:^8}|{:^8}|{:^19}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|".format(*cabecalhos))
        
        # Imprime linha horizontal para separar cabeçalhos das colunas
        print("+" + "-" * 8 + "+" + "-" * 8 + "+" + "-" * 19 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")
        
        # Imprime cada resposta do questionário formatada
        for resposta in self.respostas:
            print("|{:^8}|{:^8}|{:^18}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|{:^13}|".format(*resposta))
            
            # Imprime linha horizontal para separar as linhas de dados
            print("+" + "-" * 8 + "+" + "-" * 8 + "+" + "-" * 19 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")

# Função principal
def main():
    questionario = Questionario()
    continuar = True
    while continuar:
        continuar = questionario.coletar_informacoes()
    questionario.escrever_csv()
    questionario.exibir_resultados()

if __name__ == "__main__":
    main()
