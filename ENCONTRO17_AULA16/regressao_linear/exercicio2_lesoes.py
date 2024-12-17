import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# obter dados
try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    
    # utf-8, iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Demilitando as variáveis
    df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_culposa']]

    # Totalizando as lesões
    df_total_lesoes = df_lesoes.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_culposa']).reset_index()

    print(df_total_lesoes.head())

    print('Dados obtidos com sucesso!')

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()

# correlação
try:
    print('Calculando a correlação...')
    # excluir uma parte de valores extremos
    df_total_lesoes_cut = df_total_lesoes[df_total_lesoes['lesao_corp_dolosa'] < np.percentile(df_total_lesoes['lesao_corp_dolosa'], 95)] 
    df_total_lesoes_cut = df_total_lesoes[df_total_lesoes['lesao_corp_culposa'] < np.percentile(df_total_lesoes['lesao_corp_culposa'], 99)]

    # Arrays
    array_dolosa = np.array(df_total_lesoes_cut['lesao_corp_dolosa'])
    array_culposa = np.array(df_total_lesoes_cut['lesao_corp_culposa'])

    # correlação de pearson
    correlacao = np.corrcoef(df_total_lesoes['lesao_corp_dolosa'], df_total_lesoes['lesao_corp_culposa'])[0,1]

    print(f'Correlação: {correlacao}')

except ImportError as e:
    print(f'Erro ao calcular a correlação: {e}')
    exit()


# Regressão linear Análise Preditiva
try:
    print("Iniciando a regressão linear...")

    # pip install scikit-learn
    # SciKit-Learn é a principal biblioteca de Machine Learning para Python - 
    # LinearRegression: É responsável por criar o modelo de regressão linear
    from sklearn.linear_model import LinearRegression

    # Classe para dividir a distribuição dos dados em treino e teste
    from sklearn.model_selection import train_test_split

    # dividir os dados em treino e teste
    # Lesão dolosa (X): Variável independente - Utilizo para prever
    # Culposa (Y): Variável dependente - Prevista
    # Dividir a distribuição dos dados
    X_train, X_test, y_train, y_test = train_test_split(
                                            array_dolosa,
                                            array_culposa,
                                            test_size=0.2, # tamanho do conjunto de teste, logo o treino terá 0.8
                                            random_state=42
                                        )
    
    # Importar a classe de normalização
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()

    # Normalização dos dados de Lesão corporal dolosa (X)
    # Usa-se o método fit_transform, para transformar os dados de treino
    # em um escala de -1 a 1, onde a concentração será em torno de 0
    # A média no fit_transform tende a ser próxima de zero
    # Logo todos os dados estarão na mesma escala
    X_train = scaler.fit_transform(X_train.reshape(-1, 1))

    # Dados de teste (X_test)
    # só é necessário replicar a transformação
    # Então, não se usa o método fit_transform
    # Aqui, utiliza-se o método transform
    X_test = scaler.transform(X_test.reshape(-1, 1))

    # Criar o modelo linear
    # O modelo é onde encontraremos a função y = ax + b
    modelo = LinearRegression()

    # Treinar o modelo com os dados de treino
    # O resultado desse treino será a função y = ax + b
    # No momento do treino, utilizam-se as variáveis de treino de X e y
    modelo.fit(X_train, y_train)

    # R² Score (R2 score): Coeficiente de determinação
    # o resultado varia de 0 a 1
    # Acima de 0.7 é um bom modelo, quanto mais se aproxima de 1, melhor
    # Entre 0.5 e 0.7, é um modelo de qualidade moderada, recomenda-se verificar
    # Abaixo de 0.5, é uma modelo de qualidade duvidosa
    r2_score = modelo.score(X_test, y_test)

    print('R² Score:', r2_score)

    # array com os dados de lesões para prever a recuperação
    array_lesao_dolosa_pred = np.array([10000, 18000, 21000])

    # Normalizar os dados que serão utilizados para previsão
    array_lesao_dolosa_pred_scaled = scaler.transform(
                                array_lesao_dolosa_pred.reshape(-1, 1)
                                )

    # prever lesões corporais dolosas (próximos 3 meses)
    lesao_pred = modelo.predict(array_lesao_dolosa_pred_scaled)

    print('Previsão de lesões corporais (próximos 3 meses): ', lesao_pred)

except ImportError as e:
    print("Erro ao realizar a regressão linear: ", e)
    exit()


# avaliação do modelo
try:
    print('Avaliando o modelo de previsões...')

    plt.subplots(2, 2, figsize=(15, 5))
    plt.suptitle('Avaliação do modelo de regressão')

    #posição 1: Gráfico de dispersão entre os arrays
    # pip install seaborn
    plt.subplot(2, 2, 1)

    sns.regplot(x=array_dolosa, y=array_culposa)
    plt.title('Gráfico de dispersão')
    plt.xlabel('Lesão dolosa')
    plt.ylabel('Lesão culposa')

    plt.text(min(array_dolosa),
             max(array_culposa),
             f'Correlação: {correlacao}',
             fontsize=10)

    # posição 2: Gráfico de dispersão entre os dados reais e previsto
    plt.subplot(2, 2, 2)

    # Testar o modelo preditivo nos dados de teste
    y_pred = modelo.predict(X_test)

    # retornar os dados de teste para escala real
    X_test = scaler.inverse_transform(X_test)

    # Gráfico de dispersão sem a linha de regressão
    plt.scatter(X_test, y_test, color='blue', label='Dados reais')
    plt.scatter(X_test, y_pred, color = 'red', label='Previsões')

    plt.title('Dados reais x previstos')
    plt.xlabel('Lesões dolosas')
    plt.ylabel('Lesões culposas')

    plt.legend()

    #posição 3: Resíduos
    plt.subplot(2, 2, 3)

    # Os resíduos são a diferença entre os dados reais e previstos
    # y_teste - y_pred (Ponto de vista é a variável dependente)
    # Avaliar a qualidade do modelo
    # resíduos próximos de zero e aleatórios, 
    # Se os resíduos não forem aleatórios, logo possuem
    # um padrão, o modeo NÃO é confiável
    residuos = y_test - y_pred

    # plotar em gráfico de dispersão
    plt.scatter(y_pred, residuos)

    # adicioanar uma linha constante no 0
    plt.axhline(y=0, color='black', linewidth=2)

    plt.title('Resíduos')
    plt.xlabel('Previsões')
    plt.ylabel('Resíduos')

    # posição 4: dispersão dos valores simulados
    plt.subplot(2, 2, 4)
    
    plt.scatter(array_lesao_dolosa_pred, lesao_pred)

    plt.title('Lesões Coporais')
    plt.xlabel('Lesões dolosas simulada')
    plt.ylabel('Lesões corporais previstas')

    plt.tight_layout()
    plt.show()

except ImportError as e:
    print("Erro ao avaliar o modelo: ", e)
    exit()