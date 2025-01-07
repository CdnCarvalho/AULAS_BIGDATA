import polars as pl
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# - Constante do Endereço dos dados
ENDERECO_DADOS = r'./dados/'

# - Obtendo dados do dados_bf.parquet
try:
    print('Obtendo dados....')

    hora_inicio = datetime.now()

    # - Carregar os dados do programa Bolsa Família em formato Parquet
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # - Carregar os dados de votação no formato CSV, passando as especificações
    df_votacao = pl.read_csv(ENDERECO_DADOS + 'votacao_secao_2022_BR.csv', separator=';', encoding='iso-8859-1')

    # print(df_votacao)

    hora_fim = datetime.now()
    print('Dados obtidos com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao obter dados: ', e)
    exit()


# Iniciar processamento
try:
    print('Processando dados....')

    hora_inicio = datetime.now()

    # - Filtrando o Turno das Eleições e os Candidatos
    # - Pegando apenas os dados do 2º turno e
    # - os candidatos 13 (Lula) e 22 (Bolsonaro)
    df_votacao = df_votacao.filter(
        (pl.col('NR_TURNO') == 2) &
        (pl.col('NR_VOTAVEL').is_in([13, 22]))
    )

    # Delimitar colunas df_votacao: SG_UF, NM_VOTAVEL e QT_VOTOS
    # df_votacao = df_votacao.select(['SG_UF', 'NM_VOTAVEL', 'QT_VOTOS'])
    # --------------------------------------------------------------------

    # # converter para float o valor parcela
    # df_bolsa_familia = df_bolsa_familia.with_columns(
    #     pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    # )
    # --------------------------------------------------------------------

    # - Ativar a memória cache do Polars, que melhora a performance
    #   em grandes volumes de dados.
    # - Memória cache é a memória de acesso RÁPIDO
    # - Ativar o método StringCache, do Polars é muito útil para filtros,
    #   cálculos em dados de larga escala
    with pl.StringCache():

        '''VOTAÇÃO'''
        # Preparar o dataframe de votação em formato "lazy" para otimização
        df_votacao_lazy = df_votacao.lazy().select(['SG_UF', 'NM_VOTAVEL', 'QT_VOTOS'])

        # - Os tipos de dados categóricos são mais eficientes, que a string.
        # - Quando o tipo de dados é categórico, o Polars cria um dicionário de
        #   índices NUMÉRICOS, que otimiza o consumo de memória.
        # --------------------------------------------------------------
        
        # - Converter string para categórico
        df_votacao_lazy = df_votacao_lazy.with_columns([
            pl.col('SG_UF').cast(pl.Categorical),
            pl.col('NM_VOTAVEL').cast(pl.Categorical)
        ])

        # - Agrupar votos por estado e candidato, somando o total
        df_votacao_uf = df_votacao_lazy.group_by(['SG_UF', 'NM_VOTAVEL']).agg(pl.col('QT_VOTOS').sum())

        # - Coleta os dados
        df_votacao_uf = df_votacao_uf.collect()


        '''BOLSA FAMÍLIA'''
        # - Preparar o dataframe do Bolsa Família em formato "lazy"
        df_bolsa_familia_uf_lazy = df_bolsa_familia.lazy().select(['UF', 'VALOR PARCELA'])

        # - Converter UF para categórico
        df_bolsa_familia_uf_lazy = df_bolsa_familia_uf_lazy.with_columns(pl.col('UF').cast(pl.Categorical))

        # - Totalizar o valor das parcelas por estado
        df_bolsa_familia_uf = df_bolsa_familia_uf_lazy.group_by('UF').agg(pl.col('VALOR PARCELA').sum())

        # - Coletar dados
        df_bolsa_familia_uf = df_bolsa_familia_uf.collect()

        # - Juntar os dois dataframes. Faz o mesmo que o merge() do Pandas
        '''JOIN DOS DATAFRAMES'''
        df_votos_bolsa_familia = df_votacao_uf.join(df_bolsa_familia_uf, left_on='SG_UF', right_on='UF')
    

    # - Exibir todas as linhas de um dataframe.
    # - Evitar isso em dados de larga escala.
    pl.Config.set_tbl_rows(-1)
    print(df_votacao_uf)

    # - Ajustar formato numérico para exibição de valores
    pl.Config.set_float_precision(2)
    pl.Config.set_decimal_separator(',')
    pl.Config.set_thousands_separator('.')

    print(df_bolsa_familia_uf)

    print(df_votos_bolsa_familia)

    hora_fim = datetime.now()
    print('Dados procesados com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao processar dados: ', e)
    exit()



# - Calcular correlações entre os votos e os valores do Bolsa Família
try:
    print('Correlacionando dados....')

    hora_inicio = datetime.now() 

    # - Dicionário para armazenar as correlações por candidato
    # - Serão dois candidatos: Lula e Bolsonaro
    # - As correlações serão armazenadas em objeto chave e valor
    dict_correlacoes = {}

    for candidato in df_votos_bolsa_familia['NM_VOTAVEL'].unique():
        # - Filtrar os dados para o candidato atual
        df_candidato = df_votos_bolsa_familia.filter(pl.col('NM_VOTAVEL') == candidato)

         # - Criar arrays para os votos e valores do Bolsa Família
         #   do Bolsa Família p/ o candidato atual
        array_votos = np.array(df_candidato['QT_VOTOS'])
        array_valor_parcela = np.array(df_candidato['VALOR PARCELA'])
        
        # - Calcular o coeficiente de correlação (r)
        # - O resultado é sempre em um matriz (linha x coluna)
        #   por isso, pegamos o valor da posição 0,1. Ou seja,
        #   o valor da linha 0 e coluna 1 da matriz retornada.
        # - OBS: P/ um melhor entendimento, você pode rodar o código
        #   sem o [0, 1] e ver o resultado.
        correlacao = np.corrcoef(array_votos, array_valor_parcela)[0, 1]

        print(f'Correlção para {candidato}: {correlacao}')

        # - Adicioanr correlação ao dicionário
        dict_correlacoes[candidato] = correlacao

    hora_fim = datetime.now()
    print('Correlação realizada com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

except ImportError as e:
    print('Erro ao correlacionar dados: ', e)
    exit()


# - VISUALIZAÇÃO
try:
    print('Visualizando dados....')
    hora_inicio = datetime.now()

    plt.subplots(2, 2, figsize=(17, 7))
    plt.suptitle('Votação x Bolsa Família', fontsize=16)

    # - Gráfico 1: Ranking de votos de Lula por estado
    plt.subplot(2, 2, 1)
    plt.title('Lula')

    df_lula = df_votos_bolsa_familia.filter(pl.col('NM_VOTAVEL') == 'LUIZ INÁCIO LULA DA SILVA')

    df_lula = df_lula.sort('QT_VOTOS', descending=True)

    plt.bar(df_lula['SG_UF'], df_lula['QT_VOTOS'])


    # - Gráfico 2: Ranking de votos de Bolsonaro por estado
    plt.subplot(2, 2, 2)
    plt.title('Bolsonaro')

    df_bolsonaro = df_votos_bolsa_familia.filter(pl.col('NM_VOTAVEL') == 'JAIR MESSIAS BOLSONARO')

    df_bolsonaro = df_bolsonaro.sort('QT_VOTOS', descending=True)

    plt.bar(df_bolsonaro['SG_UF'], df_bolsonaro['QT_VOTOS'])


    # - Gráfico 3: Valor total do Bolsa Família por estado
    plt.subplot(2, 2, 3)
    plt.title('Valor Parcela')

    df_bolsa_familia_uf = df_bolsa_familia_uf.sort('VALOR PARCELA', descending=True)

    plt.bar(df_bolsa_familia_uf['UF'], df_bolsa_familia_uf['VALOR PARCELA'])


    # - Gráfico 4: Exibir as correlações calculadas
    plt.subplot(2, 2, 4)
    plt.title('Correlações')

    # - Coordenadas do plt.text com nome dos candidatos e as correlações
    x = 0.2
    y = 0.6

    for candidato, correlacao in dict_correlacoes.items():
        plt.text(x, y, f'{candidato}: {correlacao}', fontsize=12)

        # - reduzir 0.2 do eixo Y p/ ajustar a posição do texto    
        y -= 0.2   # Isso é o mesmo que: y = y - 0.2
    
    plt.axis('off')

    plt.tight_layout()

    hora_fim = datetime.now()
    print('Visualização realizada com sucesso! Tempo de processamento: ', hora_fim - hora_inicio)

    plt.show()
except ImportError as e:
    print('Erro ao visualizar dados: ', e)
    exit()