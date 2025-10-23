import pandas as pd
import warnings
from datetime import datetime
from filter_data_utils import add_tipo_column

warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

file_path = "./data/dataset.xlsx"
df = pd.read_excel(file_path, sheet_name="Relatório 1", skiprows=3)
df = df.iloc[:, 1:]
df = add_tipo_column(df)
print(df.head())

current_month = datetime.now().month
for k in range(1,10):
    df_filtered = df[df["Mês - Numérico"] == k]

    # print(df[df["Mês - Numérico"] == current_month])

    ### This lets you see the groups
    # print(df.groupby(["Tipo", "Fonte Recurso - Código"]).size())

    groups = df_filtered.groupby(["Tipo", "Fonte Recurso - Código"])

    output_path = f"./data/output_{k}.xlsx"
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for k, ((tipo, fonte), group_df) in enumerate(groups):
            # print(tipo, fonte)
            # print(group_df)
            sheet_name = f"{tipo} - Fonte {fonte}"
            group_df.to_excel(writer, sheet_name=sheet_name, index=False)
