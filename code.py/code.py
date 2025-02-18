import pandas as pd
import os
import numpy as np
from bs4 import BeautifulSoup

git 
# parsing,cleaning and extracting html files , their headers and number of columns
def extract_table (filepath):
    if not os.path.exists(filepath):
        print("there is no such file in your device")
        return []
    
    with open(filepath,"r",encoding="utf-8") as file:
        parsedfile= BeautifulSoup(file,"html.parser")
    tables= parsedfile.find_all("table")
    extractedtables=[]
    for i in tables:
        rows=i.find_all("tr")
        headr = [cell.get_text(strip=True) for cell in rows[0].find_all(["th", "td"])] if rows else []

        columns=len(headr)


#making the dataset homogenous and arranging  row data
        Data=[]
        for i in rows:
            cells = [cell.get_text(strip=True) for cell in i.find_all("td")]
            if len(cells)<columns:
                cells.extend([""]*(columns-len(cells)))
            else:
                cells=cells[:columns]
            Data.append(cells)
        df = pd.DataFrame(Data, columns=headr if headr else None)

        extractedtables.append(df)
    return extractedtables
        

html_folder = r"C:\Users\USER\Downloads\Business-Quant-Dataset-Html-Tables\Business Quant Dataset - Html Tables"
file_paths = [
    os.path.join(html_folder, "table_9.html"),
    os.path.join(html_folder, "table_12.html"),
    os.path.join(html_folder, "table_62.html")
]
for file_path in file_paths:
    tables = extract_table(file_path)

    if tables:
        print(f"\nExtracted tables from {file_path}:")
        
        for i, table in enumerate(tables):
            print(f"\nTable {i+1}:")
            print(table.head())  # Show first 5 rows
    else:
        print(f"No tables found in {file_path}")
