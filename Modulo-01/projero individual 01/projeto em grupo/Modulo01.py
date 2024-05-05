'''Detalhes do projeto:
⇨ A pesquisa que será realizada deve conter 4 perguntas (o grupo pode decidir o tema e formular as 
questões) que podem ser respondidas com Sim (1), Não (2), Não sei responder (3). 
⇨ Para iniciar o questionário, será solicitado ao usuário que informe a sua idade e gênero. Cada 
linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1, resposta_2, resposta_3, 
resposta_4, data e hora da resposta.
⇨ O projeto deve ficar solicitando respostas em um laço de repetição que fica inserindo as 
respostas informadas nas linhas do .csv até que a idade de 00 seja informada; então, podemos 
ficar inserindo novas respostas por quanto tempo for necessário (quando a idade 00 é informada 
o projeto para de executar).
⇨ Com os dados preenchidos no .csv, o grupo deve realizar uma exibição simples dos resultados 
utilizando o Excel (com uma simulação de 10 respostas no questionário para gerar os dados). Na 
apresentação, deverão ser demonstrados o funcionamento do questionário e o exemplo dos 
dados coletados.

1 - Início
Hora de planejar:
■ Criar um plano de ação. Planejamento é a parte mais importante!
■ Utilizar o tempo para descobrir o que já sabem e o que falta aprender.
■ Dividir o trabalho que será realizado para cada um dos integrantes.
■ Começar a estruturar as primeiras tarefas do projeto e definir os responsáveis.
2 - Execução
Construção do documento:
■ Colocar o planejamento em ação.
■ Começar a criar o código do projeto.
■ Verificar se o projeto está ok a cada nova iteração enviada para o repositório.
3 - Refinamento
É hora de refinar o projeto!
■ Começar a fazer a entrada das informações;
■ Testar com diferentes entradas e checar se não ocorrem erros;
■ Criar o parágrafo de evidência de entrega ao começo do GitHub;
■ Realizar o processo de teste com uma pessoa diferente da que 
desenvolveu a funcionalidade.
4 - Finalização
É hora de entregar o projeto:
■ Verificar se tudo está ok no GitHub e se todos enviaram os seus códigos 
para o repositório;
■ Entregar o projeto! Todos os integrantes devem enviar o link no Portal;
■ Se preparar para apresentação! '''



'''import csv
import datetime

class Questionario:
    def __init__(self):
        self.respostas = []
        self.perguntas = [
            "Voce ja realizou algum tipo de investimento? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Sabe como funciona o mundo de investimentos em Cripto? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Voce considera as Criptos moedas um investimento seguro? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Voce possui algum fundo de emergencia ? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Voce conhece alguem que realiza algum tipo de investimento incluindo as Criptomoedas? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Voce arriscaria a iniciar no mercado de investimentos? (1 - Sim, 2 - Não, 3 - Não sei): "
        ]

    def coletar_informacoes(self):
        idade = int(input("Digite sua idade (00 para encerrar): "))
        if idade == 00:
            return False
        genero = input("Digite seu gênero (M/F): ")
        self.inserir_resposta(idade, genero)
        return True

    def inserir_resposta(self, idade, genero):
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        respostas = [idade, genero, data_hora]
        for pergunta in self.perguntas:
            resposta = input(pergunta)
            respostas.append(resposta)
        self.respostas.append(respostas)

    def escrever_csv(self, nome_arquivo='questionario.csv'):
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Idade", "Gênero", "Data/Hora", "Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4"])
            writer.writerows(self.respostas)

    def exibir_resultados(self):
        print("Resultados do Questionário:")
        for resposta in self.respostas:
            print(resposta)

# Função principal
def main():
    questionario = Questionario()
    continuar = True
    while continuar:
        continuar = questionario.coletar_informacoes()
    questionario.escrever_csv()
    questionario.exibir_resultados()

if __name__ == "__main__":
    main()'''


import csv
import datetime
import os
import sys

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

    def coletar_informacoes(self):
        idade = int(input("Digite sua idade (00 para encerrar): "))
        if idade == 00:
            return False
        genero = input("Digite seu gênero (M/F): ")
        self.inserir_resposta(idade, genero)
        return True

    def inserir_resposta(self, idade, genero):
        data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        respostas = [idade, genero, data_hora]
        for pergunta in self.perguntas:
            resposta = input(pergunta)
            respostas.append(resposta)
        self.respostas.append(respostas)

    def escrever_csv(self, nome_arquivo='questionario.csv'):
        caminho_documentos = os.path.join(os.path.expanduser('~'), 'Documentos')
        nome_arquivo = os.path.join(caminho_documentos, nome_arquivo)
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Idade", "Genero", "Data/Hora", "Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4", "Resposta 5", "Resposta 6"])
            writer.writerows(self.respostas)

    def exibir_resultados(self):
        print("Resultados do Questionário:")
        for resposta in self.respostas:
            print(resposta)

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

