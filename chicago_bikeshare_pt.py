# coding: utf-8
# autor: Luan Fernandes (lgabs)
# Resumo do código: 
#   Trata-se de tarefas que exploram os dados de uso de bicicletas compartilhadas na região de Chicago pela empresa Divvy
#   As tarefas compõem o projeto 1 do curso de Data Science 1 da Udacity 

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista de dicionários em que os labels das features são chaves
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
# Como a lista é uma lista de dicionários, esta linha será a primeira viagem e suas informações (features). 
print("Linha 0: ")
print(data_list[0])

# Imprimindo as informações da primeira viagem (primeira linha do arquivo csv):
print("Dados da primeira viagem registrada:")
print(list(data_list[0].values()))

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for k in range(20):
    print(list(data_list[k].values()))

# Sendo uma lista de dicionários, cada índice da lista é uma viagem registrada em forma de
# dicionário. Podemos acessar as features usando os seus próprios nomes como chaves
# Exemplo: sample = data_list[k] retorna a k-ésima viagem como um dicionário. sample['Gender'] retorna o gênero.

# As features são:
# ['Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
# Impressão com a numeração para conferir as 20 amostras
for i, sample in enumerate(data_list[:20]):
    print('{:>7}: {}'.format(i+1,sample['Gender']))

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
        
# Solução: já que se optou por uma lista de dicionários, usamos diretamente o label da feature desejada.
# Para não alterar o tratamento dos asserts (que acessam a feature pelo índice e não pelo label),
# criou-se uma lista de fetaures para associar o índice de entrada com a respectiva feature 
def column_to_list(data, index: int):
    # Função para criar uma lista de valores de uma certa feature a partir do dataset.
    # Argumentos:
    #   data:  lista de dicionários com as features de cada viagem e seus valores
    #   index: índice que representa o label de uma feature
    # Retorna:
    #   feature_list: lista com os valores das features desejadas para as viagens descritas em 'data'

    feature_list = []
    features = list(data[0].keys())
    feature_list = [trip[features[index]] for trip in data]
    return feature_list

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
# TODO: Conte cada gênero. Você não deveria usar uma função para fazer isso.

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
# Por que nós não criamos uma função para fazer isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data):
    # Função para contar o número de usuários para cada gênero (Masculino ou Feminino).
    # Argumentos
    #   data: lista de dicionários com as features de cada viagem e seus valores
    # Retorna:
    #   [male,female]: uma lista com as quantidades de cada gênero

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
    # Função para determinar o gênero mais popular.
    # Argumentos:
    #   data: lista de dicionários com as features de cada viagem e seus valores
    # Retorna:
    #   answer: string com o gênero mais popular. Caso a popularidade seja igual, retorna 'Igual'.

    answer = ""
    # gerar a lista com número de homens e mulheres com função já desenvolvida count_gender
    n_genders = count_gender(data_list)  
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

input("Aperte Enter para continuar...")
# Se tudo está rodando como esperado, verifique este gráfico!
print("\nGráfico de quantidades de uso para cada gênero:")
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list) 
y_pos = list(range(len(types)))    
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o seguinte gráfico! Ele indica as quantidades de usos entre homens e mulheres")

def count_users(data):
    # Função para contar os usuários de cada tipo. 
    # Argumentos:
    #   data: lista de dicionários com as features de cada viagem e seus valores 
    # Retorna:
    #   [subscribers, customers]: lista com a quantidade de cada tipo de usuário

    subscribers = 0
    customers = 0
    for trip in data:
        if trip['User Type'] == 'Subscriber':
            subscribers += 1
        elif trip['User Type'] == 'Customer':
            customers += 1
    return [subscribers, customers]

user_list = column_to_list(data_list, 6)
user_types = ["Subscriber", "Customer"]
user_quantity = count_users(data_list) 
y_pos = list(range(len(user_types)))     
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
# Você não deve usar funções prontas para fazer isso, como max() e min().
 
def statistics_from_list(data):
    # Função que calcula estatísticas básicas das durações de viagens.
    # Argumentos:
    #   data: lista de strings representando as durações das viagens 
    # Retorna:
    #   min_trip: duração mínima das viagens
    #   max_trip: duração máxima das viagens
    #   mean_trip: média de duração das viagens
    #   median_trip: mediana da duração das viagens

    # Vamos criar uma lista de floats para operar sobre ela, pois o argumento vem em formato de string
    trip_durations = [float(i) for i in data]
    # para calcular a mediana, a lista precisa estar ordenada
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

# talvez o ideal seja o objeto se chamar 'station_type' ou 'stations', mas vou usar o sugerido.'user_types' foi recomendado acima para tipo de usuário

start_stations_list = column_to_list(data_list, 3)
user_types = list(set(start_stations_list))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
print("\nTAREFA 11: Verificação da documentação do código (ver código em um editor de texto).")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
'''
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.
'''

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"
print(answer)
        
def count_items(column_list):
    item_types = list(set(column_list)) 
    item_types.sort()  # o sort ajudará quando os types tem ordem própria (ex: meses em formato numérico ou ano de nascimento)
    count_items = []
    for item_type in item_types:
        count = []
        count = [i for i in column_list if i == item_type]
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

input("A seguir, temos as tarefas adicionais. Aperte Enter para continuar...")
# ---------------------------------------------------------
#                 PERGUNTAS ADICIONAIS
# ---------------------------------------------------------

# TAREFA 13
# Faça um gráfico mensal mostrando o uso das biciletas. 

print("\nTAREFA 13: gráfico mensal de uso das bicicletas:")
# Vamos gerar a lista de starttime e endtime e em seguida os meses:
start_datetimes = column_to_list(data_list,0)
end_datetimes = column_to_list(data_list,1)
start_month = [date[5:7] for date in start_datetimes]

# Vamos verificar se alguma rota ultrapassa um mês (ao pegar a bicicleta no final do último dia de um mês, por exemplo)
count_month_passes = 0
for i,j in zip(start_datetimes, end_datetimes):
    if i[5:7] != j[5:7]: # "Rota ultrapassa um mês!"
        count_month_passes += 1
print('Existem {} rota(s) que ultrapassam um mês (cerca de {}% do total)'.format(count_month_passes, round(count_month_passes/len(data_list)*100,6)))
# A evidência de algum caso acima distorce um pouco a contagem do uso por mês, mas no geral não deve comprometer um simples panorama dos meses de maior e menor uso 
# Assim, vamos usar como referência a lista start_month
months, month_counts = count_items(start_month)

y_pos = list(range(len(months)))     
plt.bar(y_pos, month_counts)
plt.ylabel('Quantidade')
plt.xlabel('Mês')
plt.xticks(y_pos, months)
plt.title('Quantidade de usos por mês')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 14
# Qual as estações mais populares para ínicio e fim de viagem? O número de start stations é igual ao número de end stations?

print("\nTAREFA 14: número de start/end stations e as estações mais populares:")
start_stations_types, start_stations_count = count_items(column_to_list(data_list,3))
end_stations_types, end_stations_count = count_items(column_to_list(data_list,4))

popular_start_station = {'Name': '', 'Count': 0}
popular_end_station = {'Name': '', 'Count': 0}
for elem, count in zip (start_stations_types, start_stations_count):
    if count > popular_start_station['Count']:
        popular_start_station['Name'] = elem
        popular_start_station['Count'] = count
for elem, count in zip(end_stations_types, end_stations_count):
    if count > popular_end_station['Count']:
        popular_end_station['Name'] = elem
        popular_end_station['Count'] = count

print('Start Stations: {}\nMost popular: {} ({} usos)\n'.format(len(start_stations_types), popular_start_station['Name'], popular_start_station['Count']))
print('End Stations: {}\nMost popular: {} ({} usos)'.format(len(end_stations_types), popular_end_station['Name'], popular_end_station['Count']))
print('------ Fim do Projeto 1 ------')