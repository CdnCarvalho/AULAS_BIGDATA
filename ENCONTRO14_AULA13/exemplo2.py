import polars as pl
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np


ENDERECO_DADOS = r'./dados/'

# LENDO OS DADOS DO ARQUIVO PARQUET
try:
    print('\nIniciando leitura do arquivo parquet...')

    # Pega o tempo inicial
    inicio = datetime.now()

    # TEMOS DUAS FORMAS DE LER O ARQUIVO PARQUET
    # 1 - read_parquet
    # 2 - scan_parquet

    # read_parquet é um método para ler um arquivo Parquet
    # Este método retorna um DataFrame
    # Arquivo Parquet é um arquivo binário, que permite ler e escrever dados de forma eficiente
    # Exemplo:
    # df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') 
    
    # Scan_parquet: Geralment é um método mais rápido que read_parquet,
    # pois não carrega os dados em memória imediatamente.
    # O Scan_parquet gera um plano de execução, para realizar a leitura dos dados.
    # Um plano de execução é a melhor rota para realizar a leitura dos dados, 
    # utilizando o mínimo de recursos de processamento local (memória e núcleos de processamento)    
    # Exemplo:
    df_bolsa_familia_plan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    
    # .collect: 
    # Converte o plano de execução em um DataFrame
    # O plano de execução precisa ser convertido pelo .collect() em um DataFrame, 
    # para que os dados possam ser manipulados.
    # Um plano de execução é um processo que escolhe a melhor rota para realizar a leitura dos dados,
    # e o .collect() é o método que executa esse plano de execução.
    df_bolsa_familia = df_bolsa_familia_plan.collect()
    
    print(df_bolsa_familia)

    # Pega o tempo final
    fim = datetime.now()

    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except Exception as e: 
    print(f'Erro ao ler os dados do parquet: {e}')


    # No exemplo1, os dados foram manipulados e salvos em um arquivo parquet, 
    # este processo é conhecido como pré-processamento.
    # Uma vez préprocessado, os dados podem ser lidos diretamente do arquivo parquet,
    # sem a necessidade de serem manipulados novamente para gerar as análises.
    # O processo de gerarar a análise é o que conhecemos como Processaemnto de Dados.

    # A partir daqui podemos gerar as análises dos dados, fazendo o uso das bibliotecas
    # que quisermos, como Pandas, Numpy, Matplotlib, Seaborn, etc, tendo como base de dados
    # o arquivo parquet. Como exemplo, realizamos uma demonstração plotando o Boxplot, 
    # mas antes fizemos o uso do Numpy para gerar o Array. 
    # Usar Array, em muitas das vezes, nos faz obter ganho em performance. O nosso ganho
    # é computacional. Poderíamos usar "Uma Coluna do Polars ou do Pandas", porém com
    # Arrays Numpy, podemos fazer operações mais complexas e mais rápidas.


# Visualizar a distribuição dos valores das parcelas em um boxplot
try:
    print('Visualizando a distribuição dos valores das parcelas em um boxplot...')

    # Marcar a hora de início
    hora_inicio = datetime.now()

    # Criar um Array Numpy com o valor da parcela
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

    # criar um boxplot
    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição dos valores das parcelas')

    # marcar a hora de término
    hora_fim = datetime.now()

    plt.show()

    print(f'Tempo de execução: {hora_fim - hora_inicio}')
    print('Dados visualizados com sucesso!')

except Exception as e:
    print(f'Erro ao visualizar dados: {e}')