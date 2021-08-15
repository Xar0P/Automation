import pandas as pd
import os
from .dataset import Dados
import shutil

def analysis():
    print('Fazendo a análise de dados')

    dados = Dados()

    for file in os.listdir('./Extracted/Exported/'):
        if fr'./Extracted/Exported/{file}'.endswith('xlsx'):
            df = pd.read_excel(fr'./Extracted/Exported/{file}')
        # elif fr'./Extracted/Exported/{file}'.endswith('')

        try:
            faturamento = df['Valor Final'].sum()
            dados.add_dado(faturamento)
            qtde_produtos = df['Quantidade'].sum()
            dados.add_dado(qtde_produtos)
        except Exception as e:
            print(e)

    shutil.rmtree(r'./Extracted/Exported/')

    return dados

if __name__ == "__main__":
    analysis()