# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import sys


# Vamos ler os dados como uma lista de dicionários
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    #reader = csv.reader(file_read)
    reader = csv.DictReader(file_read) 
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas. Se a lista é uma lista
# de dicionários, então esta linha será a primeira viagem e suas informações. 

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados. Se a lista é 
# uma lista de dicionários, então esta será a segunda viagem e suas informações.
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for k in range(20):
    #print(data_list[k])
    print(list(data_list[k].values()))


# Vamos mudar o data_list para remover o cabeçalho dele.
# data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

# Sendo uma lista de dicionários, cada índice da lista é uma viagem registrada em forma de
# dicionário. Podemos acessar as features usando os seus próprios nomes como chaves
# Exemplo: sample = data_list[k] retorna a k-ésima viagem. sample['Gender'] retorna o gênero.

# As features são:
# ['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']


input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# Impressão direta
#for k in range(20):
#    print(data_list[k]['Gender'])

# Impressão com a numeração para conferir as 20 amostras
for i, d in enumerate(data_list[:20]):
    print('{}: {}'.format(i+1,d['Gender']))


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

# Solução: já que se optou por uma lista de dicionários, ao ínves do índice usamos diretamente o label da feature desejada.
# Para não alterar o tratamento dos asserts, criou-se uma lista de fetaures para associar o índice de entrada com a respectiva feature 
def column_to_list(data, index):
    # data:  lista de dicionários com as mesmas chaves em cada
    # index: índice que representa uma feature
    column_list = []
    features = list(data[0].keys())
    #print(features)  
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    column_list = [trip[features[index]] for trip in data]
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------



input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

# Solução: Se não se deve utilizar uma função direta para calcular isso, vamos proceder assim:
# Ao invés de percorrer a lista de dicionários, podemos percorrer diretamente a lista de gêneros com a função anterior
male = 0
female = 0
for trip in data_list:
    if trip['Gender'] == 'Male':
        male += 1
    elif trip['Gender'] == 'Female':
        female += 1


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos:  ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------


input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data):
    # data: lista de dicionários 
    male = 0
    female = 0
    for trip in data:
        if trip['Gender'] == 'Male':
            male += 1
        elif trip['Gender'] == 'Female':
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data):
    # data: lista de dicionários 
    answer = ""
    n_genders = count_gender(data_list)  # gerar a lista com número de homens e mulheres com função já desenvolvida
    if n_genders[0] > n_genders[1]:
        answer += 'Masculino'
    elif n_genders[0] < n_genders[1]:
        answer += 'Feminino'
    else:
        answer += 'Igual'
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list) #lista
y_pos = list(range(len(types)))    #lista [0,1]
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_users(data):
    # data: lista de dicionários 
    subscriber = 0
    customer = 0
    for trip in data:
        if trip['User Type'] == 'Subscriber':
            subscriber += 1
        elif trip['User Type'] == 'Customer':
            customer += 1
    return [subscriber, customer]

user_list = column_to_list(data_list, 6)
user_types = ["Subscriber", "Customer"]
user_quantity = count_users(data_list) # lista 1x2
y_pos = list(range(len(user_types)))    # lista [0,1]
plt.bar(y_pos, user_quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque há viagens onde a informação de gênero é uma string vazia ''. Pelas 20 primeiras amostras, há viagens onde a string a 'End Station' é destacada por um sinal de asterisco e não há informações de gênero ou ano de nascimento. Assim, a soma de contagens 'Male' e 'Female' é menor que total de contagens de usos das bicicletas."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
 
def statistics_from_list(data):
    # data é uma lista de strings representando as durações das viagens
    # portanto, vamos criar uma lista de floats para operar sobre ela
    # para calcular a mediana, a lista precisa estar ordenada
    trip_durations = [float(i) for i in data]
    trip_durations.sort()
    n = len(trip_durations)
    min_trip = trip_durations[0]
    max_trip = trip_durations[0]
    mean_trip = trip_durations[0]/n
    for elem in trip_durations[1:]:
        if min_trip > elem:
            min_trip = elem
        if max_trip < elem:
            max_trip = elem
        mean_trip += elem/n
    if n%2 == 0:
        median_trip = (trip_durations[int(n/2-1)] + trip_durations[int(n/2+1-1)])/2
    else:
        median_trip = trip_durations[int((n+1)/2-1)]
    print(median_trip)
    return min_trip, max_trip, mean_trip, median_trip

min_trip, max_trip, mean_trip, median_trip = statistics_from_list(column_to_list(data_list, 2))

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

# talvez o ideal era o objeto se chamar 'station_type' ou 'stations', mas vou usar o sugerido. Havia utilizado 'user_types' acima para tipo de usuário

start_stations_list = column_to_list(data_list, 3)
print(len(start_stations_list))
print(start_stations_list[:4])
user_types = list(set(start_stations_list))


print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
      """
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = [type for type in set(column_list)]
    count_items = []
    for type in item_types:
        count = [i for i in column_list if i == type]
        count_items.append(len(count))
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------