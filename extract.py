# src/extract.py
import pandas as pd
from typing import final

@final
def extract_data(file_path: str = 'data/raw_feedbacks.csv') -> pd.DataFrame:
    """
    Simulação da etapa de Extração (E).
    Lê dados de feedback de um arquivo CSV local, simulando um Data Lake.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Extração: {len(df)} feedbacks extraídos de {file_path}")
        return df
    except FileNotFoundError:
        print(f"❌ ERRO: Arquivo não encontrado em {file_path}. Verifique a pasta 'data/'.")
        return pd.DataFrame()

# O arquivo __init__.py em src/ pode ficar vazio, mas é necessário.
