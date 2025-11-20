# src/main_pipeline.py
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    """
    Função principal que orquestra o pipeline ETL.
    """
    print("\n--- 🚀 Iniciando Pipeline ETL com IA Generativa ---")
    
    # 1. Extração (E)
    df_extracted = extract_data()
    if df_extracted.empty:
        print("🛑 Pipeline interrompido devido à falha na Extração.")
        return

    # 2. Transformação (T)
    df_transformed = transform_data(df_extracted)
    
    # 3. Carregamento (L)
    load_data(df_transformed)
    
    print("\n--- ✨ Pipeline concluído com sucesso! ---")

if __name__ == "__main__":
    run_pipeline()
