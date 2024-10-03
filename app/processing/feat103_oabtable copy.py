import tabula
import pandas as pd
import json
import os

def ReadOabTable(file_path, update_progress, check_processing, update_status, processing_complete):
    # Verificação se o arquivo existe
    if not os.path.exists(file_path):
        print("Arquivo não encontrado")
        return
    
    try:
        # Leitura do PDF
        tables = tabula.read_pdf(file_path, pages="all", multiple_tables=True)
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return
    
    json_data = []
    total_tables = len(tables)
    
    for i, table in enumerate(tables):
        if not check_processing():
            print("Processamento cancelado")
            return
        
        # Verificando se a tabela tem exatamente quatro colunas
        if table.shape[1] != 4:
            print(f"Tabela {i+1} ignorada por não ter exatamente quatro colunas")
            continue
        
        # Renomeando as colunas
        table.columns = ["Item", "Atividade", "Valor", "%"]
        
        # Substituindo valores NaN e inválidos por string vazia e mantendo o conteúdo das células intacto
        table = table.map(lambda x: " ".join(str(x).splitlines()) if pd.notna(x) else "")
        
        # Garantindo que o conteúdo das colunas não seja misturado
        for col in table.columns:
            table[col] = table[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
        
        json_data.append(table.to_dict(orient="records"))
        
        # Atualizando a barra de progresso e status
        update_progress((i + 1) / total_tables * 100)
        update_status(i + 1, total_tables)
    
    try:
        with open("oabtable.json", "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        print("Dados exportados para oabtable.json")
    except Exception as e:
        print(f"Erro ao escrever o arquivo JSON: {e}")
        return
    
    processing_complete()
