from sys import getsizeof
import time
import random
import pyodbc

sizes = range(1,100,1)

sistema_origem = input("Digite o sistema de origem:")

# Criar conexão com o banco de dados

cnx_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:algas.database.windows.net,1433;Database=Algas;Uid=parisi;Pwd=P@risiAlgas;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
cnx = pyodbc.connect(cnx_string)

# Criar cursor para executar as queries
cursor = cnx.cursor()

# Peso inicial da carga
weight = 30

# Coordenadas iniciais aleatórias
initial_latitude = random.uniform(-90, 90)
initial_longitude = random.uniform(-180, 180)

for n in sizes:
	start_time = time.time()

	#Simulação da alteração no peso da carga
	if random.randint(0, 99) == 0:
		weight = weight - 2

	#Simulação do localização em coordenadas
	latitude = initial_latitude + random.uniform(-0.01, 0.01)
	latitude = round(latitude, 4)
	longitude = initial_longitude + random.uniform(-0.01, 0.01)
	longitude = round(longitude, 4)

	#Medição do espaço utilizado pelos dados
	space = getsizeof(weight) + getsizeof(latitude) + getsizeof(longitude)
	space = space/10**3

	#Simulação do tempo de processamento da transação
	time.sleep(0.001)

	#Medição do tempo gasto na transação
	end_time = time.time()
	elapsed_time = end_time - start_time
	elapsed_time = round(elapsed_time, 4)

	# Executar query para inserir os valores de Peso da carga, tempo de execução e memória utilizada
	values = (weight, latitude, longitude, elapsed_time, space, sistema_origem)
	cursor.execute("INSERT INTO sensores (peso, latitude, longitude, tempo_exec, mem_exec, origem) VALUES (?, ?, ?, ?, ?, ?)", values)

	print(f'Valor {n} - Peso Gerado  {weight} - Latitude Gerada  {latitude} - Longitude Gerada  {longitude} - Tempo {elapsed_time} - Memória {space} KB')

# Salvar as mudanças no banco de dados
cnx.commit()

# Fechar cursor e conexão
cursor.close()
cnx.close()