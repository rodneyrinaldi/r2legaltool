import tabula
import pandas as pd
import json

def ReadOabTable(file_path, update_progress, check_processing, update_status, processing_complete):
    tables = tabula.read_pdf(file_path, pages="all", multiple_tables=True)
    json_data = []
    total_tables = len(tables)
    
    for i, table in enumerate(tables):
        if not check_processing():
            print("Processamento cancelado")
            return
        
        # Substituindo valores NaN e inválidos por string vazia
        table = table.map(lambda x: "" if pd.isna(x) else x)
        json_data.append(table.to_dict(orient="records"))
        
        # Atualizando a barra de progresso e status
        update_progress((i + 1) / total_tables * 100)
        update_status(i + 1, total_tables)
    
    with open("tabelas.json", "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    print("Dados exportados para tabelas.json")
    
    processing_complete()
