# src/load.py
import pandas as pd
import json
from typing import final

@final
def load_data(df: pd.DataFrame, output_file: str = 'data/structured_data.json'):
    """
    Simulação da etapa de Carregamento (L).
    Salva o DataFrame transformado em um arquivo JSON.
    """
    if df.empty:
        print("⚠️ Carregamento ignorado: DataFrame de entrada vazio.")
        return
        
    # Converte o DataFrame para um formato de lista de dicionários (JSON)
    data_to_load = df.to_dict(orient='records')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_to_load, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Carregamento: Dados estruturados salvos em '{output_file}'.")
