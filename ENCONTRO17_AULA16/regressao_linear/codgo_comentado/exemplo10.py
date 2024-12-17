import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from auxiliar.conexoes import obter_dados_pd

# Constante do Endereço dos dados
ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# obter dados
# comma separeted values (CSV), em português é valores separados por vírgulas
# mas, que nem sempre são vírgulas. É preciso verificar
try:
    print('Obtendo dados de ocorrências...')

    # parâmentros: endereco_arquivo, nome_arquivo, tipo_arquivo, separador
    df_ocorrencias = obter_dados_pd(ENDERECO_DADOS,'','csv',';')

    #print(df_ocorrencias.head()) #head sem valor, trará as 5 primeiras linhas

    print('Dados obtidos com sucesso!')
except Exception as e:
    print('Erro ao obter dados: ', e)
    exit()

# delimitar somente as variáveis solicitadas e totalizar
try:
    print("inciando a delimitação das variáveis e a totalização...")
    
    # cidade e roubo de veículos
    #print(df_ocorrencias.columns) # exibir o nome de todas as colunas
    df_veiculos = df_ocorrencias[['cisp','roubo_veiculo','recuperacao_veiculos']]

    # totalizar o dataframe
    df_total_veiculos = df_veiculos.groupby('cisp')\
                            .sum(['roubo_veiculo','recuperacao_veiculos']).reset_index()
    
    print(df_total_veiculos)

    print('Delimitação e totalização concluídas!')
except Exception as e:
    print("Erro ao delimitar o dataframe: ", e)
    exit()

# correlação dos dados
try:
    print('Analisando dados...')

    # excluir uma parte de valores extremos
    df_total_veiculos_cut = df_total_veiculos[
        df_total_veiculos['roubo_veiculo'] < np.percentile(df_total_veiculos['roubo_veiculo'],95)
    ] 
    df_total_veiculos_cut  =df_total_veiculos_cut[
        df_total_veiculos_cut['recuperacao_veiculos'] < np.percentile(df_total_veiculos_cut['recuperacao_veiculos'],99)
    ]

    # Arrays
    array_roubo_veiculo = np.array(df_total_veiculos_cut['roubo_veiculo'])
    array_recuperacao_veiculos = np.array(df_total_veiculos_cut['recuperacao_veiculos'])

    correlacao = np.corrcoef(array_roubo_veiculo,array_recuperacao_veiculos)[0,1]

    print('Correlação: ', correlacao)

except Exception as e:
    print("Erro ao analisar dados: ", e)
    exit()

# análise preditiva
# cujo objetivo é prever a quantidade de recuperações de veículos
# a partir da quantidade de roubos de veículos
# utilizando a Regressão linear
try:
    print("Iniciando a regressão linear...")

    # Scikit-learn: https://scikit-learn.org/stable/index.html
    # pip install scikit-learn
    # SciKit-Learn é a principal biblioteca de Machine Learning para Python

    # importar a classe de regressão linear da biblioteca
    # LinearRegression: É responsável por criar o modelo de regressão linear
    from sklearn.linear_model import LinearRegression

    # Classe para dividir a distribuição dos dados em treino e teste
    from sklearn.model_selection import train_test_split

    # dividir os dados em treino e teste
    # ela divide os dados de forma aleatória
    # Se é aleatório, toda vez que rodar, o modelo será diferente
    # Isso não é muito bom, pq impacta na consistência
    # Interferir na aleatoriedade, enquanto os dados não mudam
    # ou seja, é aleatório, porém só muda quando a distribuição muda
    # random_state para que eu sempre tenha os mesmos resultados, 
    # enquanto a distribuição de dados não for alterada
    # Parâmentro random_state = 42
    # caso queira a aleatoriedade constante. Não utilize o random_state

    # Dividir os dados de treino e teste, sabendo que
    # Roubo de veículos (X): Variável independente - Utilizo para prever
    # Recuperação de veículos (Y): Variável dependente - Prevista
    X_train, X_test, y_train, y_test = train_test_split(
                                            array_roubo_veiculo, # var. independente
                                            array_recuperacao_veiculos,# var. dependente
                                            test_size=0.2, # tamanho do conjunto de teste, logo o treino terá 0.75
                                            random_state=42 # em homenagem ao guia do mochileiro das galáxias! 
                                        )
    
    # Importar a classe de normalização
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()

    # Normalização dos dados de Roubo de Veículos (X)
    # Dados de treino
    # Usa-se o método fit_transform, para transformar os dados de treino
    # em um escala de -1 a 1, onde a concentração será em torno de 0
    # A média no fit_transform tende a ser próxima de zero
    # Logo todos os dados estarão na mesma escala
    X_train = scaler.fit_transform(X_train.reshape(-1,1))

    # Dados de teste (X_test)
    # O Scaler já foi ajustado nos dados de treino
    # Porém, é necessário ajusta os dados de teste também
    # Nesse caso, só necessário replicar a transformação
    # Então, não se usa o método fit_transform
    # Aqui, utiliza-se o método transform
    X_test = scaler.transform(X_test.reshape(-1,1))

    # Criar o modelo linear
    # O modelo é onde encontraremos a função y = ax + b
    modelo = LinearRegression()

    # Treinar o modelo com os dados de treino
    # O resultado desse treino será a função y = ax + b
    # O método fit é o responsável por treinar o modelo
    # é tentar explicar a relação entre as variáveis (X e y)
    # no momento do treino, utilizam-se as variáveis de treino de X e y
    modelo.fit(X_train, y_train)

    # Verificar a qualidade do modelo
    # nos dados de teste
    # R² Score (R2 score): Coeficiente de determinação
    # o resultado varia de 0 a 1
    # Acima de 0.7 é um bom modelo, quanto mais se aproxima de 1, melhor
    # Entre 0.5 e 0.7, é um modelo de qualidade moderada, recomenda-se verificar
    # Abaixo de 0.5, é uma modelo de qualidade duvidosa
    r2_score = modelo.score(X_test, y_test)

    print('R² Score:', r2_score)

    # array com os dados de roubo de veículos para prever a recuperação
    # 400.000, 500.000 e 600.000.
    array_roubo_veiculo_pred = np.array([400000,500000,600000])

    # Lembre-se que os dados estão normalizados
    # Normalizar os dados que serão utilizados para previsão
    array_roubo_veiculo_pred_scaled = scaler.transform(
                                array_roubo_veiculo_pred.reshape(-1,1)
                                )
    
    # prever a recuperação de veículos
    # método predict
    recup_pred = modelo.predict(array_roubo_veiculo_pred_scaled)

    print('Previsão de recuperação de veículos (próximos 3 meses): ', recup_pred)

except Exception as e:
    print("Erro ao realizar a regressão linear: ", e)
    exit()

# avaliação do modelo
try:
    print('Avaliando o modelo de previsões...')

    plt.subplots(2,2,figsize=(15,5))
    plt.suptitle('Avaliação do modelo de regressão')

    #posição 1: Gráfico de dispersão entre os arrays
    # pip install seaborn
    # https://seaborn.pydata.org/
    plt.subplot(2,2,1)

    sns.regplot(x=array_roubo_veiculo,y=array_recuperacao_veiculos)
    plt.title('Gráfico de dispersão')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperação de veículos')

    plt.text(min(array_roubo_veiculo),
             max(array_recuperacao_veiculos),
             f'Correlação: {correlacao}',
             fontsize=10)

    # posição 2: Gráfico de dispersão entre os dados reais e previsto
    # Tomando como base os dados de X (Roubo de veículo)
    # Dados reais: Eixo X - X_test / Eixo Y - y_test
    # Previstos: Eixo X - X_test / Eixo Y - y_pred
    plt.subplot(2,2,2)

    # Testar o modelo preditivo nos dados de teste
    y_pred = modelo.predict(X_test)

    # retornar os dados de teste para escala real
    X_test = scaler.inverse_transform(X_test)

    # Gráfico de dispersão sem a linha de regressão
    plt.scatter(X_test,y_test, color='blue', label='Dados reais')
    plt.scatter(X_test,y_pred, color = 'red', label='Previsões')

    plt.title('Dados reais x previstos')
    plt.xlabel('Roubo de veículos')
    plt.ylabel('Recuperações de veículos')

    plt.legend()

    #posição 3: Resíduos
    plt.subplot(2,2,3)

    # Os resíduos são a diferença entre os dados reais e previstos
    # y_teste - y_pred (Ponto de vista é a variável dependente)
    # Avaliar a qualidade do modelo
    # resíduos próximos de zero e aleatórios, 
    # para o modelo ser confiável
    # Se os resíduos não forem aleatórios, logo possuem
    # um padrão, o modeo NÃO é confiável
    # próximo a zero, nesso caso, é relativo, de acordo com
    # a magnitude do problema. Algo que seja menor 10%
    # do valor real

    # cálculo dos resíduos
    residuos = y_test - y_pred

    # plotar em gráfico de dispersão
    plt.scatter(y_pred,residuos)

    # adicioanar uma linha constante no 0
    plt.axhline(y=0, color='black', linewidth=2)

    plt.title('Resíduos')
    plt.xlabel('Previsões')
    plt.ylabel('Resíduos')

    # posição 4: dispersão dos valores simulados
    plt.subplot(2,2,4)
    
    plt.scatter(array_roubo_veiculo_pred, recup_pred)

    plt.title('Recuperações de veículos simuladas')
    plt.xlabel('Roubo veículo simulado')
    plt.ylabel('Recuperação de veículo prevista')

    plt.tight_layout()
    plt.show()

except Exception as e:
    print("Erro ao avaliar o modelo: ", e)
    exit()