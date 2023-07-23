# Script para retornar o dataframe na pasta data 
import os 
import glob


# função para fazer o carregamento de dados 
def get_processing_data():
    FOLDER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    XLSX_FILE = glob.glob(os.path.join(FOLDER_PATH, "*.xlsx"))[0]
    return XLSX_FILE
