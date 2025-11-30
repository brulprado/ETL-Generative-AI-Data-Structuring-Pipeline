# ETL-Generative-AI-Data-Structuring-Pipeline
Pipeline ETL em Python que utiliza simulação de LLM para transformar dados textuais brutos (feedback) em um formato estruturado pronto para BI

**Autora:** Bruna Lima Prado

# 🚀 ETL de Alto Desempenho com IA Generativa para Estruturação de Dados Não Estruturados

## Visão Geral

Este projeto demonstra a construção de um pipeline de **Engenharia de Dados (ETL)** robusto e desacoplado, utilizando a filosofia de **IA Generativa** para transformar dados textuais brutos e não estruturados (Feedback de Clientes) em dados tabulares prontos para Business Intelligence (BI).

Em um contexto onde o volume de dados textuais excede a capacidade de análise manual, a solução substitui métodos complexos de NLP por um único componente de **Large Language Model (LLM)**, focado em **Data Structuring**. Para garantir portabilidade, eficiência e controle de custos, a transformação LLM é simulada de forma local, preparada para migrar facilmente para soluções *on-premise* como **Llama 3** ou **Mistral** via vLLM.

## 🎯 Desafio de Negócio & Inovação

### O Problema
A complexidade de analisar milhares de feedbacks de clientes diariamente resulta em alto *time-to-insight* e custos operacionais elevados. Regras tradicionais de Processamento de Linguagem Natural (NLP) são frágeis e exigem manutenção constante.

### A Solução (O Brilho)
Implementamos uma arquitetura de pipeline que encapsula a lógica de negócio na fase de transformação. O componente de IA Generativa não apenas extrai o sentimento, mas também **cria categorias e resumos sintéticos**, transformando uma *string* de texto em uma linha de dados totalmente estruturada e consumível.

* **Zero-Shot Structuring:** A IA realiza a categorização sem treinamento prévio (simulando um *prompt* eficiente).
* **Desacoplamento:** O pipeline é independente de APIs externas (como OpenAI), focando em uma solução escalável e controlável em ambiente de produção.

## 🧠 Arquitetura do Pipeline (ETL)

O pipeline segue a estrutura clássica E-T-L, com foco na modularidade e resiliência:

### 1. **E**xtraction (`src/extract.py`)
* **Fonte de Dados:** Simulação de extração de uma fonte de dados massiva (e.g., S3/Data Lake) via arquivo CSV.
* **Função:** Coleta de `id_feedback`, `id_produto` e o campo crucial de `texto_feedback` bruto.

### 2. **T**ransformation (`src/transform.py`)
* **Tecnologia:** Simulação de um **LLM local** (função heurística robusta).
* **Processo:**
    * **Análise de Sentimento:** Classificação em Positivo, Negativo ou Neutro.
    * **Classificação Temática:** Categorização em Performance, Design ou Preço.
    * **Resumo Sintético:** Geração de um resumo conciso do feedback.
* **Robustez:** Implementação de `try...except` e *fallbacks* para simular resiliência contra falhas de inferência ou *rate limits*.

### 3. **L**oad (`src/load.py`)
* **Destino:** Carregamento dos dados estruturados em formato JSON (simulando um *staging area* ou um **Data Warehouse** como Snowflake/BigQuery).
* **Formato:** Dados prontos para consumo por ferramentas de BI (Tableau, PowerBI).

## 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python 3.10+
* **Bibliotecas:** Pandas (Processamento de Dados), JSON (Carregamento).
* **Conceitos Arquiteturais:** Modularização de Código (Sênior), Resiliência e Tratamento de Exceções, Data Structuring com LLMs.
* **Ferramentas:** Apache Airflow/Prefect (Orquestração), Docker (Empacotamento), vLLM/Ollama (Inferência Otimizada).

## ⚙️ Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter Python instalado.

1.  **Clone o Repositório:**
    ```bash
    git clone [(https://github.com/brulprado)]
    cd ETL-Generative-AI-Feedback-Analysis
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # ou venv\Scripts\activate no Windows
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Pipeline Principal:**
    ```bash
    python src/main_pipeline.py
    ```
    O resultado estruturado será salvo em `data/structured_data.json`.

## 📊 Análise de Resultados (Data Storytelling)

Consulte o notebook **`notebooks/ETL_Data_Storytelling.ipynb`** para uma visualização completa.

| Atributo | Antes (Dados Brutos) | Depois (Dados Estruturados) |
| :--- | :--- | :--- |
| **Formato** | Texto Livre (`string`) | JSON/Tabular (`dict`) |
| **Valor** | Não Acionável | Sentimento, Categoria, Resumo |
| **Exemplo de Valor Agregado** | *O preço é alto, mas a performance compensa.* | **Sentimento:** Positivo | **Categoria:** Preço/Performance |
