# Projeto de Armazenamento de Dados de Pesquisa em Python

## Descrição
Este projeto foi desenvolvido como parte de uma atividade proposta ao nosso Squad. O objetivo era criar uma aplicação capaz de armazenar dados coletados em uma pesquisa em um arquivo .csv, para possibilitar análises futuras. A pesquisa consiste em um levantamento ativo realizado pelos funcionários da empresa, que saem às ruas para coletar as respostas.

O tema da pesquisa é sobre um assunto relevante no momento atual: as criptomoedas e os investimentos relacionados a elas. As perguntas incluem questões sobre o conhecimento do entrevistado sobre esse tipo de investimento, se já investiu ou pretende investir, entre outras. O objetivo é coletar informações dos entrevistados para análises posteriores.

## Detalhes do Projeto
- A pesquisa consiste em 6 perguntas que podem ser respondidas com "Sim" (1), "Não" (2) ou "Não sei responder" (3).
- Para iniciar o questionário, é solicitado ao usuário que informe sua idade e gênero. Cada linha do arquivo .csv contém: idade (apenas números), gênero (apenas M ou F), respostas às perguntas e data/hora da resposta.
- As respostas são inseridas em um laço de repetição que continua até que a idade "00" seja informada. Isso permite a inserção de novas respostas quantas vezes forem necessárias. Quando a idade "00" é informada, o programa para de executar.
- Os dados preenchidos no .csv podem ser visualizados e analisados no Excel ou em outras ferramentas de análise de dados.

## Instruções de Uso
1. Clone ou baixe este repositório para o seu computador.
2. Certifique-se de ter Python instalado em sua máquina.
3. Execute o script Python `questionario.py`.
4. Siga as instruções apresentadas para responder às perguntas da pesquisa.
5. Quando solicitado, insira a idade "00" para encerrar o questionário.
6. Os dados serão armazenados em um arquivo `questionario.csv` no diretório atual.
7. Os dados podem ser abertos e analisados em aplicativos como Excel.

## Tecnologias Utilizadas
- Python
- CSV
- Datetime


## Partes do Código com Explicações Técnicas

### Função `criar_csv(self, Documentos='questionario.csv')`
Esta função é responsável por criar um arquivo CSV vazio com o nome especificado ou `questionario.csv` por padrão. Ela utiliza a biblioteca `csv` do Python para escrever os cabeçalhos das colunas no arquivo.

### Python
def criar_csv(self, Documentos='questionario.csv'):
    diretorio_atual = os.getcwd()
    nome_arquivo = os.path.join(diretorio_atual, Documentos)
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(["Idade", "Genero", "Data/Hora", "Resposta 1", "Resposta 2", "Resposta 3", "Resposta 4", "Resposta 5", "Resposta 6"])

Função coletar_informacoes(self)
Esta função é responsável por solicitar a idade e o gênero do usuário, e então inserir as respostas às perguntas da pesquisa. Ela utiliza um loop while para continuar solicitando informações até que a idade informada seja "00".


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


Função escrever_csv(self, Documentos='questionario.csv')
Esta função é responsável por adicionar as respostas coletadas ao arquivo CSV. Ela recebe as respostas como entrada e as escreve no arquivo CSV, utilizando a biblioteca csv do Python.

def escrever_csv(self, Documentos='questionario.csv'):
    diretorio_atual = os.getcwd()
    nome_arquivo = os.path.join(diretorio_atual, Documentos)
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(self.respostas)
    print(f"Dados adicionados ao arquivo CSV {nome_arquivo}")


Função exibir_resultados(self)
Esta função é responsável por exibir os resultados do questionário de forma legível. Ela formata os dados em uma tabela e os imprime no console.


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

## Autor
1 - Hebert Garcia da Silva
2 - Guilherme de Albuquerque Sousa
3 - Valdeilson Souza de Carvalho
4 - Pedro Souza

---


<h2>Pedro:

<p></p>
<img src="img/pedro.png"width= "300px">
<p></p>
<p> <a href="https://github.com/devpedrosou" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" style="border-radius: 30px"></a> </p>
   
<p>  <a href="https://www.linkedin.com/in/pedro-souza-a382b3182" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px"></a> </p>
 </h2>
<h2>Valdeilson:
<p></p>
<img src="img/vau.png"width= "300px">
<p></p>
<p>  <a href="https://github.com/VALdeilSONn" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" style="border-radius: 30px"></a> </p>

<p>  <a href="https://www.linkedin.com/in/valdeilson-souza-de-carvalho-8871b5245/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px"></a> </p></h2>
   
<h2>Hebert:
<p></p>
<img src="img/hebert.png"width= "300px">
<p></p>
<p>  <a href="https://github.com/HebertGarcia" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" style="border-radius: 30px"></a> </p>
 
<p>  <a href="https://www.linkedin.com/in/hebert-garcia-baa97213b/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px"></a> </p></h2>


<h2>Guilherme:
<p></p>
<img src="img/guilherme.png"width= "300px">
<p></p>
<p>  <a href="https://github.com/GuilhermeASousa" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" style="border-radius: 30px"></a> </p>
   
<p>  <a href="https://www.linkedin.com/in/guilhermeasousa/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px"></a> </p></h2>



Este README inclui seções detalhadas sobre o projeto, instruções de uso, tecnologias utilizadas, partes do código com explicações técnicas e informações sobre o autor. Sinta-se à vontade para personalizar conforme necessário!
