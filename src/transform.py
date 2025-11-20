# src/transform.py
import pandas as pd
from typing import final

def _simulate_llm_structuring(texto: str) -> pd.Series:
    """
    SIMULAÇÃO DO LLM (Data Structuring):
    Analisa o texto e retorna dados estruturados.
    """
    texto_lower = texto.lower()
    
    # Simulação de Sentimento
    if any(k in texto_lower for k in ["adorei", "excelente", "ótimo", "superou"]):
        sentimento = "Positivo"
    elif any(k in texto_lower for k in ["desapontado", "fraca", "sem graça", "alto para"]):
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"
        
    # Simulação de Categoria
    if any(k in texto_lower for k in ["bateria", "performance", "rápido", "jogos"]):
        categoria = "Performance"
    elif any(k in texto_lower for k in ["design", "cor", "material"]):
        categoria = "Design/Estética"
    elif "preço" in texto_lower:
        categoria = "Custo"
    else:
        # Faltava este else na sua imagem
        categoria = "Geral" 
        
    # Simulação de Resumo (extração de frase chave, simulando um LLM)
    resumo = texto.split('.')[0].strip() + "..." 
    
    return pd.Series([sentimento, categoria, resumo], 
                     index=['Sentimento', 'Categoria', 'Resumo_IA'])


@final
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica a lógica de Transformação de IA (simulada) ao DataFrame,
    garantindo resiliência na aplicação da função de inferência.
    """
    if df.empty:
        print("⚠️ Transformação ignorada: DataFrame de entrada vazio.")
        return df
        
    print("⏳ Transformação: Aplicando modelo LLM (simulado)...")
    
    try:
        # Aplica a função de simulação em todos os feedbacks
        df[['Sentimento', 'Categoria', 'Resumo_IA']] = df['texto_feedback'].apply(_simulate_llm_structuring)
        
        # Limpeza/Normalização
        df_transformed = df.drop(columns=['texto_feedback'])
        
        print("✅ Transformação concluída. Dados estruturados adicionados.")
        return df_transformed
        
    except Exception as e:
        print(f"❌ ERRO GRAVE na Transformação: {e}. Retornando DataFrame original.")
        return df
