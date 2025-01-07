import chardet
import pandas as pd


# # Detectar a codificação do arquivo CSV
# try:
#     # with open('./dados/csv/isp/BaseDPEvolucaoMensalCisp.csv', 'rb') as f:
#     #     resultado = chardet.detect(f.read())
#     # print(f"Codificação detectada: {resultado['encoding']}")
# except ImportError as e:
#     print(f"Erro ao ler o arquivo com a codificação do arquivo: {e}")
#     exit()


# # Ler o arquivo CSV com a codificação detectada
# try:
#     # with open('./dados/csv/votacao/votacao_secao_2022_BR.csv', 'rb') as f:
#     #     resultado = chardet.detect(f.read())
#     # print(f"Codificação detectada: {resultado['encoding']}")
# except ImportError as e:
#     print(f"Erro ao ler o arquivo com a codificação do arquivo: {e}")
#     exit()


# Ler o arquivo CSV com a codificação iso-8859-1 detectada
try:
    # Ler e Salvar com a codificação UTF-8
    df = pd.read_csv('./dados/csv/votacao/votacao_secao_2022_BR.csv', sep=';', encoding='iso-8859-1')  # Substitua 'utf-8' pela codificação detectada, se diferente
    df.to_csv('votacao_secao_2022_BR_2.csv', sep=';', index=False, encoding='utf-8')

    # # Salvar o DataFrame em um novo arquivo CSV com codificação ISO-8859-1
    # df.to_csv('dados_isp_modificado1.csv', index=False, encoding='utf-8')
except ImportError as e:
    print(f"Erro ao converter a codificação do arquivo: {e}")
    exit()



# Verificar o tamanho dos dados nos campos da coluna DS_LOCAL_VOTACAO_ENDERECO
try:
    # Leia o arquivo novamente
    df = pd.read_csv('votacao_secao_2022_BR_2.csv', sep=',', encoding='utf-8')

    # Verifique os tamanhos dos valores na coluna problemática
    max_length = df['DS_LOCAL_VOTACAO_ENDERECO'].str.len().max()
    print(f"Tamanho máximo: {max_length}")

    # Filtre os valores grandes
    print(df[df['DS_LOCAL_VOTACAO_ENDERECO'].str.len() > 255])
except ImportError as e:
    print(f"Erro ao verificar o tamanho das séries: {e}")
    exit()
