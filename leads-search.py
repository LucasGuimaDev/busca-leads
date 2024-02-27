
import pandas as pd
import re
import os
from unidecode import unidecode

### mudar o caminho da pasta que contém os arquivos excel

pasta =  '''caminho da pasta com os arquivos em excel'''

arquivos = os.listdir(pasta)

arquivos_xlsx = [arquivo for arquivo in arquivos if arquivo.endswith('.xlsx')]

# o código abaixo itera sobre os arquivps da pasta e realiza o tratamento um por vez

for arquivo in arquivos_xlsx:
    
    caminho_arquivo = os.path.join(pasta, arquivo)

    df = pd.read_excel(caminho_arquivo, engine='openpyxl')


    colunas_excluidas = ['YQ4gaf src', 'OSrXXb', 'rllt__details', 'yi40Hd', 'RDApEe', 'BI0Dve', 'if66xd', 'BI0Dve 2']
    colunas_a_concatenar = [coluna for coluna in df.columns if coluna not in colunas_excluidas]

    df['detalhes'] = df[colunas_a_concatenar].apply(lambda x: ''.join(str(valor) for valor in x), axis=1)

    df = df[['OSrXXb', 'rllt__details', 'yi40Hd', 'detalhes']]
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.rename(columns={'OSrXXb':'nome', 'rllt__details':'ramo'})
    df = df[['nome', 'ramo', 'detalhes']]

    df['end'] = df['detalhes'].apply(lambda end: str(end.split(sep='·')[0].strip())).str.replace('Fechado', '').str.replace('Aberto', '').str.replace('Fecha em breve às ', '')
    df['end'] = df['end'].apply(lambda end: str(end.split(sep=' ⋅')[0].strip())).str.lower()
    df['end'] = df['end'].apply(lambda x: unidecode(x))

    df['tel'] = df['detalhes'].apply(lambda tel: tel.split(sep='· ')[-1].strip())
    df['tel'] = df['tel'].apply(lambda tel: tel.split(sep=' ⋅ ')[0].strip())
    df['tel'] = df['tel'].str.replace('(', '').str.replace(')', '').str.replace('-', '').str.replace(' ', '')

    df['nome'] = df['nome'].apply(lambda x: unidecode(x)).str.lower()

    df['ramo'] = df['ramo'].apply(lambda tel: tel.split(sep='· ')[-1].strip())
    df['ramo'] = df['ramo'].apply(lambda x: unidecode(x)).str.lower()


    # identifica se o numero de telefone é um numero de telefone válido
    
    padrao_telefone = re.compile(r'(?:(?:\+?([1-9]{2}))? ?(?:\(?([1-9][0-9])\)? ?)?(?:([2-8]|9[1-9])[0-9]{3})-?([0-9]{4}))')

    def extrair_telefone(texto):
        match = padrao_telefone.search(texto)
        if match:
            return match.group()
        else:
            return None

    df['tel'] = df['tel'].apply(extrair_telefone)

    df = df[['nome', 'ramo', 'end', 'tel']]


    arquivo = arquivo.replace('.xlsx', '')
    
    ### mudar o caminho do aquivo da pasta dos arquivos csv abaixo
    df.to_csv(f'-----caminho da pasta com os arquivos csv-----/{arquivo}.csv', index=False, encoding='utf-8', sep=';')
  
    print(f"Dados do arquivo {arquivo}:")
