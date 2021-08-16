import pandas as pd
import os
from .dataset import Dados
import shutil

def analysis():
    print('Fazendo a análise de dados')

    dados = Dados()

    paste_extracted = os.path.isdir('lib/data/Extracted')

    if not paste_extracted:
        os.mkdir('lib/data/Extracted')

    for file in os.listdir('lib/data/Extracted/Exported/'):
        if fr'lib/data/Extracted/Exported/{file}'.endswith('xlsx'):
            df = pd.read_excel(fr'lib/data/Extracted/Exported/{file}')
        # elif fr'./Extracted/Exported/{file}'.endswith('')

        faturamento = df['Valor Final'].sum()
        dados.add_dado(faturamento)
        qtde_produtos = df['Quantidade'].sum()
        dados.add_dado(qtde_produtos)

    # Remover a pasta
    shutil.rmtree(r'lib/data/Extracted/')

    return dados

if __name__ == "__main__":
    analysis()