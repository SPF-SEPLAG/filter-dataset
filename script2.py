import pandas as pd
import numpy as np
# Lista de feriados nacionais e facultativos de 2024
feriados_2024 = [
    "2024-02-12", "2024-02-13", "2024-02-14",
    "2024-03-28", "2024-03-29",
    "2024-04-21",
    "2024-05-01", "2024-05-30", "2024-05-31",
    "2024-08-15", "2024-08-16",
    "2024-09-07", "2024-10-12", "2024-10-28",
    "2024-11-02", "2024-11-15", "2024-11-20",
    "2024-12-08", "2024-12-24", "2024-12-25", "2024-12-31"
]
feriados_np = [np.datetime64(f) for f in feriados_2024]
# Carregar a aba 'Planilha 2'
arquivo = "Analise processual 2024 - Controle DCF 1.xlsx"
df = pd.read_excel(arquivo, sheet_name="Planilha2")
# Converter colunas para datetime
df['EMISSÃO'] = pd.to_datetime(df['EMISSÃO'], errors='coerce')
df['ENTRADA'] = pd.to_datetime(df['ENTRADA'], errors='coerce')
# Calcular dias úteis
df['Dias úteis entre a emissão da NF e entrada na DCF'] = df.apply(
    lambda row: np.busday_count(row['EMISSÃO'].date(), row['ENTRADA'].date(), holidays=feriados_np)
    if pd.notnull(row['EMISSÃO']) and pd.notnull(row['ENTRADA']) else np.nan,
    axis=1
)
# Salvar novo arquivo
df.to_excel("Analise_processual_com_dias_uteis_emissao_entrada.xlsx", index=False)
print("Arquivo gerado com sucesso.")