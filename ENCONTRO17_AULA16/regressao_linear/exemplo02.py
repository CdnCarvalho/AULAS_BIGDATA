# Caso a pasta dados ou outros pacotes não estejam no mesmo diretório,
# você pode adicionar o caminho completo para a pasta, realizando as
# devidas alterações no código. Exemplo:
# import sys
# import os
# sys.path.append(os.path.abspath('../'))
#  ------------------------------------------------------------------

# Import dos pacotes
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''Imports das funções de conexão com os dados'''
from auxiliar.conexoes import obter_dados_pd
# from auxiliar.conexoes import obter_dados_pl
# from auxiliar.conexoes import obter_dados_mysql
#  ------------------------------------------------------------------


'''Ex: Constante com os endereços dos arquivos. Só precisamos de um deles'''
ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
# ENDERECO_DADOS = './dados/csv/bolsa_fam/'
# ENDERECO_DADOS = './dados/csv/isp/'
# ENDERECO_DADOS = './dados/excel/'
#  ------------------------------------------------------------------

# Obter dados
try:
    print('Obtendo dados de ocorrências...')

    # - Os valores nem sempre são separados por vírgulas. É preciso verificar!
    # - Uso da função obter_dados_pd, importada do arquivo conexoes.py,
    #   que está na pasta auxiliar.
    # - É obrigatório passar o endereço do arquivo, o nome do arquivo, o
    #   tipo do arquivo e o separador.
    # - No 1º exemplo abaixo, o nome do arquivo está vazio. Mesmo assim,
    #   é necessário passar o valor ''.    
    '''Dados com Pandas'''
    df_ocorrencias = obter_dados_pd(ENDERECO_DADOS, '', 'csv', ';')
    # df_ocorrencias = obter_dados_pd(ENDERECO_DADOS, 'BaseDeDados_auxilio.xlsx', 'excel', ';')
    # df_ocorrencias = obter_dados_pd(ENDERECO_DADOS, 'BaseDPEvolucaoMensalCisp.csv', 'csv', ';')
    #  ------------------------------------------------------------------


    '''Dados com Polars'''
    # Para o arquivo Excel com Polars: # pip install fastexcel
    # df_ocorrencias = obter_dados_pl(ENDERECO_DADOS, '', 'csv', ';')
    # df_ocorrencias = obter_dados_pl(ENDERECO_DADOS, 'BaseDados.xlsx', 'excel', ';')
    # df_ocorrencias = obter_dados_pl(ENDERECO_DADOS, '202402_NovoBolsaFamilia.csv', 'csv', ';')
    #  ------------------------------------------------------------------


    '''Dados do Banco de Dados MySQL'''
    # - Query "Consulta" para buscar os dados
    # query = 'SELECT * FROM basedpevolucaomensalcisp LIMIT 50'
    # df_ocorrencias = obter_dados_mysql(query)
    #  ------------------------------------------------------------------


    '''ATENÇÃO'''
    # IMPORTANTE: Em todos os casos acima, deve se importar, apenas as funções
    # necessárias para evitar consumo excessivo de processamento, assim como,
    # ajustar corretamente o Endereço dos Dados p/ que funcione.
    # A ideia, é que você escolha a melhor forma de obter os dados, de acordo
    # com a sua necessidade. E que apenas substitua os trechos de código
    # necessários, NÃO mantendo os vários comentários de exemplo que ficaram
    # apenas como demonstração.
    #  ------------------------------------------------------------------

    print(df_ocorrencias)

    print('Dados obtidos com sucesso!')
except ImportError as e:
    print('Erro ao obter dados: ', e)
    exit()


# - Delimitar somente as variáveis solicitadas e totalizar
try:
    print("inciando a delimitação das variáveis e a totalização...")

    # - Imprimir o nome das colunas, para maiores conhecimentos
    # print(df_ocorrencias.columns)
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # - Totalizar os dados
    # - Agrupa os dados no DataFrame df_veiculos pela coluna 'cisp'.
    # - Calcula a soma das colunas 'roubo_veiculo' e 'recuperacao_veiculos'
    #   para cada grupo.
    # - Restaura o índice do DataFrame para que a coluna 'cisp' volte a
    #   ser uma coluna regular.
    df_total_veiculos = df_veiculos.groupby('cisp').sum(['roubo_veiculo', 'recuperacao_veiculos']).reset_index()
    
    print(df_total_veiculos)
    print('Delimitação e totalização concluídas!')

except ImportError as e:
    print("Erro ao delimitar o dataframe: ", e)
    exit()


# - Verificando a Correlação dos dados
try:
    print('Analisando dados...')

    # - Excluir uma parte de valores extremos
    # - Filtra removendo os valores da coluna 'roubo_veiculo' e
    #   'recuperacao_veiculo', que estão nos 5% mais altos.
    # - Esses filtros são aplicados para evitar que outliers influenciem de
    #   forma desproporcional a análise de correlação
    df_total_veiculos_cut = df_total_veiculos[df_total_veiculos['roubo_veiculo'] < np.percentile(df_total_veiculos['roubo_veiculo'], 95)] 
    df_total_veiculos_cut = df_total_veiculos_cut[df_total_veiculos_cut['recuperacao_veiculos'] < np.percentile(df_total_veiculos_cut['recuperacao_veiculos'], 95)]

    # - Arrays
    array_roubo_veiculo = np.array(df_total_veiculos_cut['roubo_veiculo'])
    array_recuperacao_veiculos = np.array(df_total_veiculos_cut['recuperacao_veiculos'])

    # - calcula a correlação de Pearson entre os arrays roubo e recuperacao.
    # - np.corrcoef: Retorna a matriz de correlação entre as variáveis.
    # - [0, 1]: Extrai o valor da correlação entre as duas variáveis.
    correlacao = np.corrcoef(array_roubo_veiculo, array_recuperacao_veiculos)[0, 1]

    print('Correlação: ', correlacao)

except ImportError as e:
    print("Erro ao analisar dados: ", e)
    exit()

# - Análise Preditiva
# - O objetivo é prever a quantidade de recuperações de veículos
# - a partir da quantidade de roubos de veículos utilizando a Regressão linear
try:
    print("Iniciando a regressão linear...")

    # - Instalar a biblioteca scikit-learn
    # - pip install scikit-learn
    # - SciKit-Learn é a principal biblioteca de Machine Learning para Python
    # - Documentação da biblioteca: https://scikit-learn.org/stable/
    # - --------------------------------------------------------------------

    # - Importar a classe de regressão linear da biblioteca
    # - Este import pode ser feito no início do código preferencialmente
    # - Estamos realizando aqui para facilitar o entendimento
    # - LinearRegression: É responsável por criar o modelo de regressão linear
    from sklearn.linear_model import LinearRegression

    # - Esta classe será utilizada para dividir a distribuição dos dados em:
    # - Dados de Treino e Dados de Teste
    from sklearn.model_selection import train_test_split

    # Dividir os dados em treino e teste:
    # - O treino é usado para ensinar o modelo.
    # - O teste é usado para avaliar o desempenho do modelo.
    # - --------------------------------------------------------------------

    # - A divisão é feita de forma aleatória.
    # - Isso significa que, se rodarmos o código várias vezes, os dados podem
    #   ser divididos de maneiras diferentes.
    # - Divisões diferentes podem levar a resultados ligeiramente diferentes
    #   no modelo, o que dificulta a comparação.
    # - --------------------------------------------------------------------

    # - Para garantir consistência, usamos o parâmetro `random_state`.
    # - Ele "controla" a aleatoriedade:
    # - A divisão dos dados será sempre a mesma enquanto os dados
    #   não forem alterados.
    # - Sem o `random_state`, a divisão seria sempre diferente a cada execução.
    # - --------------------------------------------------------------------

    # - Roubo de veículos (X): Variável Independente
    #   (dados usados como entrada para prever algo).
    # - Recuperação de veículos (Y): Variável Dependente
    #   (resultado que queremos prever).
    X_train, X_test, y_train, y_test = train_test_split(
                                            array_roubo_veiculo,  # Variável Independente (entrada)
                                            array_recuperacao_veiculos,  # Variável dependente (saída)
                                            test_size=0.2,  # 20% dos dados serão usados para teste; o restante (80%) será para treino.
                                            random_state=42  # Garante que a divisão seja sempre igual. O valor 42 foi usado apenas como exemplo.
                                        )
    
    # Importar a classe de normalização
    from sklearn.preprocessing import StandardScaler

    # - Cria um objeto scaler da classe StandardScaler,
    #   que será usado p/ padronizar os dados
    scaler = StandardScaler()

    # - Normalização dos dados de Roubo de Veículos (X)
    # - São os Dados de treino
    # - Usa-se o método fit_transform, para transformar os dados de treino
    #   em um escala de -1 a 1, onde a concentração será em torno de 0.
    # - A média no fit_transform tende a ser próxima de zero e o
    #   desvio padrão próximo de 1.
    # - Logo todos os dados estarão na mesma escala
    X_train = scaler.fit_transform(X_train.reshape(-1, 1))


    # Transformação dos dados de teste (X_test):
    # - O StandardScaler já foi ajustado (fit) aos dados de treino.
    # - Agora, precisamos aplicar a mesma transformação aos dados de teste.
    # - Importante: não usamos fit_transform nos dados de teste,
    #   pois isso recalibraria o scaler, causando inconsistências.
    # - Em vez disso, utilizamos apenas transform para aplicar a escala
    #   aprendida nos dados de treino.
    X_test = scaler.transform(X_test.reshape(-1, 1))

    # Criar o modelo linear
    # O modelo LinearRegression() é onde encontramos a função y = ax + b
    modelo = LinearRegression()

    # Treinando o modelo com os dados de treinamento:
    # - Utilizamos o método fit() para ajustar o modelo aos dados fornecidos.
    # - O modelo aprende a relação entre as variáveis independentes (X_train)
    #   e a variável dependente (y_train).
    # - No caso de uma Regressão Linear, o modelo determinará os coeficientes
    #  (a) e o intercepto (b) na equação: y = ax + b.
    # - O resultado desse treino será o retorno da função y = ax + b
    # - No treino, utilizam-se as variáveis de treino de X e y
    # - Após o treinamento, o modelo estará preparado para fazer previsões com novos dados.
    modelo.fit(X_train, y_train)

    # - R² Score (R2 score): Coeficiente de Determinação
    # - Verifica a qualidade do modelo
    # - O resultado varia entre 0 e 1
    # - Acima de 0.7 é um bom modelo, quanto mais, se aproxima de 1, melhor...
    # - Entre 0.5 e 0.7, é um modelo de qualidade moderada, recomenda-se verificar
    # - Abaixo de 0.5, é uma modelo de qualidade duvidosa
    r2_score = modelo.score(X_test, y_test)

    print('R² Score:', r2_score)

    # - Array com os dados de roubo de veículos para prever a recuperação, 
    #   pedida no enunciado
    array_roubo_veiculo_pred = np.array([400000, 500000, 600000])

    # - Os dados do conjunto já foram normalizados, anteriormente usando um scaler.
    # - Para manter a consistência, precisamos normalizar os novos dados de previsão 
    #   usando o mesmo scaler, que foi usado no conjunto de treinamento
    array_roubo_veiculo_pred_scaled = scaler.transform(array_roubo_veiculo_pred.reshape(-1, 1))


    # - Realizar a previsão da recuperação de veículos com o modelo treinado
    # - O método 'predict' utiliza os dados de entrada (array_roubo_veiculo_pred_scaled)
    #   para gerar uma estimativa de recuperação de veículos com base no que o modelo aprendeu
    recup_pred = modelo.predict(array_roubo_veiculo_pred_scaled)

    print('Previsão de recuperação de veículos (próximos 3 meses): ', recup_pred)

except ImportError as e:
    print("Erro ao realizar a regressão linear: ", e)
    exit()


# Avaliação do Modelo
try:
    print('Avaliando o modelo de previsões...')

    plt.subplots(2, 2, figsize=(15, 5))
    plt.suptitle('Avaliação do modelo de regressão')


    # - Posição 1: 
    # - Gráfico de Dispersão entre os arrays "Seaborn"
    plt.subplot(2, 2, 1)

    # - Instalar a biblioteca seaborn
    # - pip install seaborn
    sns.regplot(x=array_roubo_veiculo, y=array_recuperacao_veiculos)
    plt.title('Gráfico de dispersão')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperação de veículos')

    # - Posiciona o valor da correlação no canto superior esquerdo do gráfico
    plt.text(min(array_roubo_veiculo),  # Posição X do texto (menor valor do eixo X)
             max(array_recuperacao_veiculos),  # Posição Y do texto (maior valor do eixo Y)
             f'Correlação: {correlacao}',  # O texto que será exibido
             fontsize=10)  # Tamanho da fonte do texto


    # - Posição 2: Gráfico de Dispersão entre os dados Reais e Previsto "Matplotlib"
    # - Dados Reais:
    #   Eixo X: X_test
    #   Eixo Y: y_test

    # - Dados Previstos:
    #   Eixo X: X_test
    #   Eixo Y: y_pred
    plt.subplot(2, 2, 2)

    # - Usar o modelo treinado para fazer previsões
    #   com os dados de teste (X_test) "Fora do Enunciado".
    # - Isso nos permite comparar as previsões com os
    #   valores reais que conhecemos
    y_pred = modelo.predict(X_test)

    # - Retornar os dados de teste para escala Real
    # - Como os dados foram normalizados anteriormente para treinar o modelo,
    #   agora precisamos converter os valores de volta para a escala original
    #   usando o mesmo scaler, para que as comparações façam sentido
    X_test = scaler.inverse_transform(X_test)

    # - Gráfico de Dispersão sem a Linha de Regressão (Matiplotlib)
    # - Criar gráfico comparando valores reais e previstos:
    # - Pontos azuis mostram os dados reais que temos
    # - Pontos vermelhos mostram o que o modelo previu
    plt.scatter(X_test, y_test, color='blue', label='Dados reais')
    plt.scatter(X_test, y_pred, color = 'red', label='Previsões')

    plt.title('Dados reais x previstos')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperações de veículos')

    plt.legend()


    # - Posição 3: Resíduos
    plt.subplot(2, 2, 3)

    # - Resíduos:
    # - Calcular os resíduos: (erros) do modelo
    #   residuos = y_teste - y_pred
    # - Objetivo: Avaliar a qualidade do modelo
    # - Ponto de vista é a Variável Dependente
    # - Resíduo é a diferença "subtração" entre os valores reais (y_test) e as previsões (y_pred)
    # - Um bom modelo deve ter resíduos:
    #   - Próximos de zero (erros pequenos)
    #   - Distribuídos aleatoriamente (sem padrões visíveis)
    #   - Igualmente dispersos acima e abaixo de zero
    residuos = y_test - y_pred

    # - Plotar em Gráfico de Dispersão - "Matplotlib"
    plt.scatter(y_pred, residuos)

    # - Adicionar uma linha horizontal no y=0.
    # - Esta linha ajuda a visualizar, se os resíduos estão bem distribuídos
    #   acima e abaixo de zero (o que é desejável)
    plt.axhline(y=0, color='black', linewidth=2)

    plt.title('Resíduos')
    plt.xlabel('Previsões')
    plt.ylabel('Resíduos')

    
    # - Posição 4: Gráfico de Dispersão dos valores simulados "Matplotlib".
    # - Respondendo ao enunciado
    plt.subplot(2, 2, 4)
    
    # Gráfico de Dispersão dos valores simulados, em resposta ao enunciado
    plt.scatter(array_roubo_veiculo_pred, recup_pred)

    plt.title('Recuperações de veículos simuladas')
    plt.xlabel('Roubo veículo simulado')
    plt.ylabel('Recuperação de veículo prevista')

    # Ajusta o layout para evitar sobreposição dos elementos
    plt.tight_layout()
    plt.show()

except ImportError as e:
    print("Erro ao avaliar o modelo: ", e)
    exit()